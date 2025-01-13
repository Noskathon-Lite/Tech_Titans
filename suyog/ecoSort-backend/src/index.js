import dotenv from "dotenv";
import connectDb from "./db/index.js";
import app from "./app.js";
import { createServer } from "http";
import { WebSocketServer } from "ws";
import { SerialPort } from "serialport";
import { ReadlineParser } from "@serialport/parser-readline";

// Load environment variables
dotenv.config({ path: "./.env" });

// Environment Variables
const SERIAL_PORT = process.env.SERIAL_PORT || "COM9";
const PORT = process.env.PORT || 4000;

// WebSocket Message Types
const MESSAGE_TYPES = {
  CLASSIFY: "classify",
  ARDUINO_DATA: "arduino-data",
  ERROR: "error",
  ACKNOWLEDGE: "acknowledge",
};

// Create HTTP server
const server = createServer(app);

// Set up WebSocket server
const wss = new WebSocketServer({ server });

// Initialize SerialPort and parser for Arduino communication
let sPort;
try {
  if (!SERIAL_PORT) {
    throw new Error("Serial port not configured. Set the SERIAL_PORT environment variable.");
  }

  sPort = new SerialPort({
    path: SERIAL_PORT,
    baudRate: 9600,
  });

  const parser = sPort.pipe(new ReadlineParser({ delimiter: "\n" }));
  const broadcastMessage = (message) => {
    wss.clients.forEach((client) => {
        client.send(JSON.stringify(message));
      
    });
  };
  // Listen for data from Arduino
  parser.on("data", (data) => {
    const trimmedData = data.trim();
    console.log(`Arduino: ${trimmedData}`);


    // Broadcast data to all connected WebSocket clients
    wss.clients.forEach((client) => {
      if (client.readyState === client.OPEN) {
        client.send(JSON.stringify({ type: MESSAGE_TYPES.ARDUINO_DATA, data: trimmedData }));
      }
    });

    if (trimmedData === "FULL") {
      console.log("Trash is full! Notifying clients...");
      broadcastMessage({
        type: "trash_status",
        status: "full",
        message: "The trash bin is full! Please empty it.",
      });
    } else if (trimmedData === "OK") {
      console.log("Trash is not full.");
      broadcastMessage({
        type: "trash_status",
        status: "ok",
        message: "The trash bin has space.",
      });
    }
  });

  sPort.on("open", () => {
    console.log(`Serial port (${SERIAL_PORT}) opened successfully.`);
  });

  sPort.on("error", (err) => {
    console.error(`Serial port error: ${err.message}`);
  });
} catch (error) {
  console.error(`Error setting up serial port: ${error.message}`);
}

// WebSocket server connection handling
wss.on("connection",  (ws) => {
  console.log("Frontend connected via WebSocket");

  ws.on("message",  (message) => {
    try {
      const parsedMessage = JSON.parse(message);
      const { type, modelClass, detectClass } = parsedMessage;
  
      // Ensure the message type is correct
      if (type === MESSAGE_TYPES.CLASSIFY) {
        const validClassifications = ["biodegradable", "non_biodegradable"];
        if (!validClassifications.includes(modelClass)) {
          ws.send(
            JSON.stringify({ type: MESSAGE_TYPES.ERROR, message: "Invalid model class type" })
          );
          console.error("Invalid model class type received:", modelClass);
          return;
        }
  
        // Log the detectClass for later tracking or processing
        if (!detectClass) {
          ws.send(
            JSON.stringify({ type: MESSAGE_TYPES.ERROR, message: "Missing detect class in message" })
          );
          console.error("Missing detect class in message");
          return;
        }
        console.log(`Received detect class: ${detectClass}`);
  
        if (!sPort || !sPort.isOpen) {
          ws.send(
            JSON.stringify({
              type: MESSAGE_TYPES.ERROR,
              message: "Serial port is not open or available",
            })
          );
          console.error("Serial port is not open or available");
          return;
        }
  
        const command = modelClass === "biodegradable" ? "D\n" : "N\n";
        sPort.write(command, (err) => {
          if (err) {
            ws.send(
              JSON.stringify({
                type: MESSAGE_TYPES.ERROR,
                message: "Failed to write to serial port",
              })
            );
            console.error("Error writing to serial port:", err.message);
            return;
          }
          console.log(`Sent '${command.trim()}' to Arduino`);
          ws.send(
            JSON.stringify({
              type: MESSAGE_TYPES.ACKNOWLEDGE,
              message: `Command '${command.trim()}' sent to Arduino`,
            })
          );
          // const userID = req?.user._id;
          // const user = await User.findById(userID);
          // const dustbinId = req.params.id;

          // if (!user) {
          //   throw new ApiError(404, "User not found");
          // }const waste = await Waste.create({
          //   category,
          //   type,
          //   dustbinId: dustbinId,
          // });
          // if(!waste){
          //   throw new ApiError(400, "Waste not added");
          //  }
          // Optionally store detectClass for future use
          // Example: Log or process detectClass here
        });
      } else {
        ws.send(
          JSON.stringify({ type: MESSAGE_TYPES.ERROR, message: "Unknown message type" })
        );
        console.error("Unknown message type received:", type);
      }
    } catch (err) {
      ws.send(
        JSON.stringify({ type: MESSAGE_TYPES.ERROR, message: "Failed to process message" })
      );
      console.error("Error processing message:", err.message);
    }
  });
  

  ws.on("close", () => {
    console.log("Frontend disconnected");
  });
});

// Start the server
connectDb()
  .then(() => {
    server.listen(PORT, () => {
      console.log(`Server is running on http://localhost:${PORT}`);
    });
  })
  .catch((error) => {
    console.error("Error connecting to the database:", error);
  });
