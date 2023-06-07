import cv2
import numpy as np

img = cv2.imread("IMG.jpg")
print(img.shape)
img = np.zeros((512,512,3), np.uint8)
print(img.shape) 
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (255,0,0),3)
cv2.rectangle(img, (0,0), (100,150), (0,0,255), 3) 
cv2.circle(img, (400,50),30, (255,255,0),3)
cv2.imshow("Image",img) 


imgResize = cv2.resize(img,(1000,500))
imgCropped = img[0:120 , 120:360]

cv2.imshow("Original Image",img)
#cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)

cv2.waitKey(0)


