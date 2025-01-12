import cv2
import random
import numpy as np
import time
from ultralytics import YOLO
import os

print("Current Working Directory:", os.getcwd())

script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the trained model
model = YOLO("C:/my-codes/Projects/ecoSort/ecoSort-backend/ecoSort-ai/runs/classify/train2/weights/last.pt")

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use 0 for laptop camera

# Check if the video capture is opened
if not cap.isOpened():
    print("Error: Cannot access the camera")
    exit()

file_path = os.path.join(script_dir, "utils/category.txt")

# Read the class names from category.txt
with open(file_path, "r") as my_file:
    class_list = my_file.read().split("\n")

# Frame dimensions and rectangle size
frame_wid = 740
frame_hyt = 580
rect_wid, rect_hyt = 300, 300  # Width and height of the rectangle

last_model_time = time.time()
model_delay = 2  # Process the model every 2 seconds
last_label = ""  # Store the last label to display continuously

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Get frame dimensions
    h, w, _ = frame.shape

    # Define rectangle coordinates (centered)
    cx, cy = w // 2, h // 2  # Center of the frame
    x1, y1 = cx - rect_wid // 2, cy - rect_hyt // 2
    x2, y2 = cx + rect_wid // 2, cy + rect_hyt // 2

    # Ensure rectangle is within bounds
    x1, y1, x2, y2 = max(0, x1), max(0, y1), min(w, x2), min(h, y2)

    # Draw rectangle on the frame
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Crop the rectangle area
    cropped_frame = frame[y1:y2, x1:x2]

    current_time = time.time()
    if current_time - last_model_time >= model_delay:
        last_model_time = current_time
        # Convert cropped frame to RGB for the model
        input_frame = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB)

        # Perform inference
        results = model.predict(source=input_frame, save=False, conf=0.5)

        # Process results
        if results:
            for result in results:
                cls_probs = result.probs
                class_id = cls_probs.top1  # Get top-1 class
                confidence = cls_probs.top1conf.item()  # Confidence of the top-1 class
                last_label = f"{class_list[class_id]}: {confidence:.2f}"

    # Draw label on the full frame
    if last_label:
        cv2.putText(frame, last_label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display the frame with the rectangle and label
    cv2.imshow('Camera Feed', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.getWindowProperty('Camera Feed', cv2.WND_PROP_VISIBLE) < 1:
        print("Window closed by clicking the 'X' button.")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
