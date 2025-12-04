import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Draw a rectangle: cv2.rectangle(image, top-left, bottom-right, color, thickness)
    cv2.rectangle(frame, (50, 50), (200, 200), (0, 255, 0), 3)

    # Draw a circle: cv2.circle(image, center, radius, color, thickness)
    cv2.circle(frame, (300, 300), 50, (0, 0, 255), -1)  # filled circle

    # Draw a line: cv2.line(image, start_point, end_point, color, thickness)
    cv2.line(frame, (0, 0), (400, 400), (255, 0, 0), 5)

    # Put text
    cv2.putText(frame, "OpenCV Shapes", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Video with Shapes", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
