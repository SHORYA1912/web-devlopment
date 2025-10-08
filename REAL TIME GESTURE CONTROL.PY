import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not found")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break
    hsv = cv2 .cvtColor(frame, cv2.COLOR_BGR2RGB)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8) 
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest_contour) > 1000:
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Gesture Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            center_x = x + w // 2
            center_y = y + h // 2

            cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)

            cv2.imshow("Gesture Control", frame)
            cv2.imshow("filtered", result)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

cap.release()
cv2.destroyAllWindows()