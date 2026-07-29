<img width="1046" height="577" alt="image" src="https://github.com/user-attachments/assets/4508f29a-1012-4f71-836b-3a5083ea3a45" /><div align="center">

# 🛡️ GuardianAI - Intrusion Detection System

### 🚨 AI-Powered Smart Home Intrusion Detection using Python & OpenCV

Detects unauthorized entry, captures evidence, records video, and instantly sends Telegram alerts.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

</div>

---

# 📖 Overview

GuardianAI is an AI-powered smart surveillance module that monitors a predefined door region and immediately alerts the owner whenever an intrusion is detected.

The system automatically:

- 🚨 Detects motion inside the protected door region
- 📸 Captures an evidence snapshot
- 🎥 Records a 10-second video
- 📲 Sends instant Telegram notifications
- 🔊 Plays an alarm
- 🕒 Stores the event with date and time

---

# ✨ Features

| Feature | Status |
|----------|--------|
| 🚶 Motion Detection | ✅ |
| 🚪 Door ROI Detection | ✅ |
| 🚨 Intrusion Alert | ✅ |
| 📸 Snapshot Capture | ✅ |
| 🎥 Automatic Video Recording | ✅ |
| 📲 Telegram Notifications | ✅ |
| 🔊 Alarm Sound | ✅ |
| 🕒 Timestamp Logging | ✅ |

---

# 🖼️ Demo

><img width="967" height="521" alt="image" src="https://github.com/user-attachments/assets/e44e9c81-e7a2-407e-bf4e-a90b0f6f61ea" />




## Telegram Alert

![Telegram](<img width="767" height="445" alt="image" src="https://github.com/user-attachments/assets/393577b0-6a5c-40c5-9ab9-8ab00c51633b" />
g)

---

# ⚙️ Tech Stack

- 🐍 Python
- 👁️ OpenCV
- 🔢 NumPy
- 🤖 Telegram Bot API

---

# 📂 Project Structure

```text
GuardianAI-Intrusion-Detection
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── telegram_alert.py
│   ├── door_polygon.npy
│   └── alarm.wav
│
├── output/
│
├── assets/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🚀 Installation

```bash
git clone https://github.com/yourusername/GuardianAI-Intrusion-Detection.git

cd GuardianAI-Intrusion-Detection

pip install -r requirements.txt
```

---

# ▶️ Run

```bash
python src/main.py
```

---

# 🔄 Workflow

```text
Camera
   │
   ▼
Motion Detection
   │
   ▼
Door ROI Check
   │
   ▼
Intrusion Detected
   │
   ├────────► 🔊 Alarm
   ├────────► 📸 Snapshot
   ├────────► 🎥 Record Video
   └────────► 📲 Telegram Alert
```

---

# 📸 Output

```
output/
├── intruder_20260729_103501.jpg
└── intrusion_20260729_103501.mp4
```

---

# 💡 Future Enhancements

- 🎯 YOLOv8 Person Detection
- 👤 Face Recognition
- 🔥 Fire & Smoke Detection
- 🚶 Fall Detection
- 📱 Android Companion App
- ☁️ Cloud Storage
- 📊 Live Monitoring Dashboard

---

# 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

If you find this project useful, feel free to **⭐ Star** the repository.

---

# 📜 License

This project is licensed under the **MIT License**.

---

<div align="center">

### ⭐ If you like this project, don't forget to Star the repository ⭐

Made with ❤️ using Python & OpenCV

</div>
