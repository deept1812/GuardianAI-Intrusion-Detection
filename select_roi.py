import cv2
import numpy as np
door_polygon = np.load("door_polygon.npy")

VIDEO_PATH = r"C:\Users\User\OneDrive\Desktop\project\GuardianAi\src\CCTV caught the thief Thief in house - Interesting facts vlogs (720p, h264).mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

points = []

def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append((x, y))

cv2.namedWindow("Select Door")
cv2.setMouseCallback("Select Door", mouse)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    display = frame.copy()

    if len(points) > 0:
        cv2.polylines(display, [np.array(points)], False, (0,255,255), 2)

    if len(points) == 4:
        door_polygon = np.array(points, dtype=np.int32)

        cv2.polylines(display, [door_polygon], True, (0,255,255), 3)

        cv2.putText(display,
                    "Press S to Save",
                    (20,70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,255,0),
                    2)

    cv2.putText(display,
                "Click 4 door corners",
                (20,30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,255,255),
                2)

    cv2.imshow("Select Door", display)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s") and len(points) == 4:
        np.save("door_polygon.npy", door_polygon)
        print("Door saved!")
        break

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()