from ultralytics import YOLO
import cv2
import cvzone
import math

cap = cv2.VideoCapture("./videos/bikes.mp4") # For video

model = YOLO("../Yolo_weights/yolov8n.pt")


try:
    while True:
        success, img = cap.read()
        if not success:
            print("Failed to grab frame")
            break
            
        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding box coordinates
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1
                
                # Draw box 
                cvzone.cornerRect(img, (x1, y1, w, h))
                
                # Confidence score
                conf = math.ceil(box.conf[0] * 100)
                cls = int(box.cls[0])
                
                # Draw label
                cvzone.putTextRect(img, f'{model.names[cls]} {conf}%', 
                                 (max(0, x1), max(35, y1-10)),
                                 scale=1, thickness=1)

        cv2.imshow("Image", img)
        
        # Break loop with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Clean up
    cap.release()
    cv2.destroyAllWindows()