import requests
from config import BOT_TOKEN, CHAT_ID


def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        requests.post(url, data=data, timeout=10)
        print("Telegram message sent.")
    except Exception as e:
        print("Message Error:", e)


def send_photo(photo_path):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    try:
        with open(photo_path, "rb") as photo:
            requests.post(
                url,
                data={"chat_id": CHAT_ID},
                files={"photo": photo},
                timeout=20
            )
        print("Photo sent.")
    except Exception as e:
        print("Photo Error:", e)


def send_video(video_path):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"

    try:
        with open(video_path, "rb") as video:
            requests.post(
                url,
                data={"chat_id": CHAT_ID},
                files={"video": video},
                timeout=60
            )
        print("Video sent.")
    except Exception as e:
        print("Video Error:", e)


def send_intrusion_alert(photo_path=None, video_path=None):

    message = (
        "🚨 GuardianAI Alert\n\n"
        "Intrusion Detected!\n\n"
        "📍 Location: Main Door\n"
        "📸 Snapshot Captured\n"
        "🎥 Recording Started\n"
        "Please check immediately."
    )

    send_message(message)

    if photo_path:
        send_photo(photo_path)

    if video_path:
        send_video(video_path)