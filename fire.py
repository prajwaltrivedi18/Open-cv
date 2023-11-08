import cv2
import smtplib
import playsound
import threading

def play():
		playsound.playsound('audio.mp3')
fire_cascade=cv2.CascadeClassifier("fire_detection.xml")
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fire=fire_cascade.detectMultiScale(gray,1.2,5)
    for x,y,w,h in fire:
        cv2.rectangle(frame,(x+20,y+20),(x+w-20,y+h-20),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+h]
        print("Alert! Fire Detected!")
        # playsound('D:/opencv/audio.mp')
        # x = vlc.MediaPlayer('audio.mp3')
        # x.play()
        # webbrowser("audio.mp3")
        threading.Thread(target=play).start()
    cv2.imshow("Fire detected",frame)
    if cv2.waitKey(1)==13:
        break
cap.release()
    # cv2.destroyAllWindows()