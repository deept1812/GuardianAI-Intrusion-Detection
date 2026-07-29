# main1.py
# GuardianAI integrated version
import os,time,cv2,numpy as np
from datetime import datetime
try:
    import winsound
    SOUND=True
except:
    SOUND=False
from config import *
from telegram_alert import send_message,send_photo,send_video

VIDEO_PATH=r"C:\Users\User\OneDrive\Desktop\project\GuardianAi\src\CCTV caught the thief Thief in house - Interesting facts vlogs (720p, h264).mp4"

os.makedirs(OUTPUT_FOLDER,exist_ok=True)
door_polygon=np.load(DOOR_FILE)
cap=cv2.VideoCapture(VIDEO_PATH)
fps=cap.get(cv2.CAP_PROP_FPS)
if fps<=1: fps=20
W=int(cap.get(3)); H=int(cap.get(4))
fgbg=cv2.createBackgroundSubtractorMOG2(history=500,varThreshold=25,detectShadows=False)
kernel=np.ones((5,5),np.uint8)
intrusion=False; recording=False; writer=None; telegram_sent=False

while True:
    ret,frame=cap.read()
    if not ret: break
    out=frame.copy()
    cv2.polylines(out,[door_polygon],True,(0,255,255),3)
    mask=fgbg.apply(frame)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    cs,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    enter=False
    for c in cs:
        if cv2.contourArea(c)<MIN_AREA: continue
        x,y,w,h=cv2.boundingRect(c)
        if w<MIN_WIDTH or h<MIN_HEIGHT: continue
        cx=x+w//2; cy=y+h//2
        if cv2.pointPolygonTest(door_polygon.astype(np.float32),(float(cx),float(cy)),False)>=0:
            enter=True
            cv2.rectangle(out,(x,y),(x+w,y+h),(0,255,0),2)
    if enter and not intrusion:
        intrusion=True
        now=datetime.now()
        stamp=now.strftime("%Y%m%d_%H%M%S")
        photo=os.path.join(OUTPUT_FOLDER,f"intruder_{stamp}.jpg")
        video=os.path.join(OUTPUT_FOLDER,f"intrusion_{stamp}.mp4")
        cv2.imwrite(photo,frame)
        if SOUND and os.path.exists("alarm.wav"):
            winsound.PlaySound("alarm.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
        msg=f"""🚨 GUARDIANAI ALERT 🚨

⚠️ Intruder Entered

🏠 {HOUSE_ADDRESS}

📅 {now.strftime('%d-%m-%Y')}
🕒 {now.strftime('%I:%M:%S %p')}

🚪 Main Door"""
        send_message(msg)
        send_photo(photo)
        writer=cv2.VideoWriter(video,cv2.VideoWriter_fourcc(*'mp4v'),fps,(W,H))
        recording=True
        start=time.time()
    if recording:
        writer.write(out)
        if time.time()-start>=RECORD_SECONDS:
            writer.release(); writer=None; recording=False
            if not telegram_sent:
                send_video(video); telegram_sent=True
    if intrusion:
        cv2.putText(out,'INTRUSION DETECTED',(20,40),0,1,(0,0,255),2)
    cv2.imshow('GuardianAI',out)
    if cv2.waitKey(30)&0xff==ord('q'): break
if writer: writer.release()
cap.release()
cv2.destroyAllWindows()
