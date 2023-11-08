# # detect frontal face the image
# import cv2
# img=cv2.imread("pic2.jpeg")
# cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces=cascade.detectMultiScale(gray,1.1,6)
# #coordinates of faces
# for x,y,w,h in faces:
#     img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv2.imshow("Face Detected",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import cv2
cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#accessing the camera
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(gray,1.03,6)
    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
    cv2.imshow("FACE",frame)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()