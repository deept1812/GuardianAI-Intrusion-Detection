
import cv2
import numpy as np
import os
from datetime import datetime

VIDEO_PATH = r"C:\Users\User\OneDrive\Desktop\project\GuardianAi\src\CCTV caught the thief Thief in house - Interesting facts vlogs (720p, h264).mp4"
DOOR_FILE = "door_polygon.npy"   # change to src/door_polygon.npy if required
MIN_AREA = 800

door_polygon = np.load(DOOR_FILE)

cap = cv2.VideoCapture(VIDEO_PATH)

fgbg = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=25,
    detectShadows=False
)

kernel = np.ones((5,5), np.uint8)
os.makedirs("output", exist_ok=True)

snapshot_saved = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    annotated = frame.copy()

    cv2.polylines(annotated,[door_polygon],True,(0,255,255),3)
    cv2.putText(annotated,"DOOR",tuple(door_polygon[0]),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)

    mask = fgbg.apply(frame)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=2)

    contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    intrusion = False

    for cnt in contours:
        if cv2.contourArea(cnt) < MIN_AREA:
            continue

        x,y,w,h = cv2.boundingRect(cnt)
        cx = x + w//2
        cy = y + h//2

        cv2.rectangle(annotated,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.circle(annotated,(cx,cy),5,(0,0,255),-1)

        if cv2.pointPolygonTest(
            door_polygon.astype(np.float32),
            (float(cx),float(cy)),
            False
        ) >= 0:

            intrusion = True

            if not snapshot_saved:
                filename = "output/intruder_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
                cv2.imwrite(filename, frame)
                print("Snapshot saved:", filename)
                snapshot_saved = True

    if intrusion:
        cv2.putText(annotated,"INTRUSION DETECTED",(20,50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        cv2.rectangle(annotated,(0,0),
                      (annotated.shape[1]-1,annotated.shape[0]-1),
                      (0,0,255),5)
    else:
        snapshot_saved = False

    cv2.imshow("GuardianAI - Motion Intrusion", annotated)
    cv2.imshow("Motion Mask", mask)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
