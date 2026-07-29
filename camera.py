from ultralytics import YOLO
import cv2

# -----------------------------
# Load Models
# -----------------------------
# These files are in the GuardianAi folder
person_model = YOLO("../yolov8n.pt")
bag_model = YOLO("../best.pt")

print("Person Model:", person_model.names)
print("Bag Model:", bag_model.names)

# -----------------------------
# Camera
# -----------------------------
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # -----------------------------
    # Detect & Track People
    # -----------------------------
    person_results = person_model.track(
        frame,
        persist=True,
        classes=[0],      # person only
        conf=0.5,
        verbose=False
    )

    # -----------------------------
    # Detect & Track Bags
    # -----------------------------
    bag_results = bag_model.track(
        frame,
        persist=True,
        conf=0.25,
        verbose=False
    )

    # -----------------------------
    # Draw People
    # -----------------------------
    output = person_results[0].plot()

    # -----------------------------
    # Draw Bags on same frame
    # -----------------------------
    output = bag_results[0].plot(img=output)

    cv2.imshow("GuardianAI", output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()