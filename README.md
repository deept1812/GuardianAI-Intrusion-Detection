# GuardianAI-Intrusion-Detection
AI-powered intrusion detection system using Python, OpenCV, motion detection, ROI-based monitoring, Telegram alerts, snapshot capture, and automatic video recording.

# GuardianAI - Intrusion Detection System

An AI-powered intrusion detection system developed using Python and OpenCV for smart home security.

## Features

- Motion Detection
- Door ROI (Polygon Boundary)
- Intrusion Detection
- Snapshot Capture
- 10-Second Video Recording
- Telegram Alert Notification
- Alarm Sound
- Timestamp Logging

## Technologies

- Python
- OpenCV
- NumPy
- Telegram Bot API

## Project Structure

src/
- main.py
- config.py
- telegram_alert.py
- door_polygon.npy

output/
- Captured snapshots
- Recorded videos

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python src/main.py
```

## Workflow

1. Define the door region.
2. Detect motion.
3. Check whether motion enters the selected ROI.
4. Trigger an alarm.
5. Save a snapshot.
6. Record a 10-second video.
7. Send alerts through Telegram.

## Future Improvements

- YOLO Person Detection
- Multi-Person Tracking
- Face Recognition
- Cloud Database Integration
- Mobile Application

## License

MIT License
