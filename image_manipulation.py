import cv2
import numpy as np

img = cv2.imread("IMG.jpg")
kernel = np.ones((5,5),np.uint8)


cv2.imshow("IMG",img)

imGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imGray,(7,7),0)
imgCanny = cv2.Canny(img,500,500)
imgDialation = cv2.dilate(imgCanny,kernel,iterations = 1)
imgEroded = cv2.erode(imgDialation,kernel,iterations = 1)

cv2.imshow("Grey Image",imGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)