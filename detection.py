
import cv2
img=cv2.imread("photo2.jpg")
cv2.imshow("This is an image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
while True:
    if cv2.waitKey(1)==ord('a'):
        break
cv2.destroyAllWindows()

