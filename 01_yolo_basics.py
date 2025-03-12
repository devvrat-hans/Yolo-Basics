from ultralytics import YOLO
import cv2
import os
import math

# Initialize YOLO model
model = YOLO("./Yolo_weights/yolov8n.pt")

# Read and process image
img = cv2.imread("./Images/2.png")
results = model(img)

# Process and draw detections
for r in results:
    boxes = r.boxes
    for box in boxes:
        # Get box coordinates
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        
        # Draw rectangle
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        
        # Add confidence score and class name
        conf = math.ceil(box.conf[0] * 100)
        cls = int(box.cls[0])
        class_name = model.names[cls]
        
        # Draw label
        label = f'{class_name} {conf}%'
        cv2.putText(img, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.5, (255, 0, 255), 2)

# Display results
cv2.imshow("Detection", img)
key = cv2.waitKey(0)
cv2.destroyAllWindows()