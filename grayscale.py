#to convert rgb to grayscale
# method 1
# import cv2
# img=cv2.imread("photo2.jpg",0)
# cv2.imshow("Gray scale image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows
#method 2
# import cv2
# img=cv2.imread("photo2.jpg")
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray scale image",gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#converting gray scale image to binary
import cv2
img=cv2.imread("pic.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#convert gray to binary
ret,binary=cv2.threshold(gray,1,255,cv2.THRESH_BINARY)
cv2.imshow("Binary image",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

