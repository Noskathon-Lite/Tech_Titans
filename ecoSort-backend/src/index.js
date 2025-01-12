import dotenv from "dotenv";
import connectDb from "./db/index.js";
import app from "./app.js";
import { Server } from "socket.io";
import { createServer } from "http";
import { PythonShell } from "python-shell";

dotenv.config({
    path: "./.env"
});

// Create HTTP server and integrate it with socket.io
const server = createServer(app);
const io = new Server(server, {
    cors: {
        origin: "*", // Replace with your frontend's URL for security
        methods: ["GET", "POST"]
    }
});

// WebSocket integration
io.on("connection", (socket) => {
    console.log("Client connected:", socket.id);

    // Handle start-camera event from the frontend
    socket.on("start-camera", () => {
        console.log("Start-camera event received from client");

        let options = {
            mode: "text",
            pythonOptions: ["-u"], // Get output in real-time
            scriptPath: "ecoSort-ai",
            args: []
        };

        const pyshell = new PythonShell("wasteManagement.py", options);

        // Send real-time output from Python to the client
        pyshell.on("message", (message) => {
            console.log("Real-time message from Python:", message);
            socket.emit("camera-data", message); // Real-time data
        });

        // Handle Python script completion
        pyshell.end((err, code, signal) => {
            if (err) {
                console.error("Error executing Python script:", err);
                socket.emit("camera-error", "Error executing script");
                return;
            }
            console.log("Python script finished.");
            socket.emit("camera-complete", "Script execution completed");
        });
    });

    // Handle disconnection
    socket.on("disconnect", () => {
        console.log("Client disconnected:", socket.id);
    });
});

// Start the server and connect to the database
const port = process.env.port || 4000;
connectDb()
    .then(() => {
        server.listen(port, () => {
            console.log("Server is running on port", port);
        });
    })
    .catch((error) => {
        console.log("Error connecting to the database:", error);
    });
