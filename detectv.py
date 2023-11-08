import cv2
import matplotlib.pyplot as plt 

cap=cv2.VideoCapture(0)
ret,frame=cap.read()
plt.imshow(frame)
plt.title("Face detected")
plt.show()
cap.release()

