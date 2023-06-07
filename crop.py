#Crop and Resize
import cv2
import numpy as np

img = cv2.imread("IMG.jpg")
print(img.shape)

imgResize = cv2.resize(img,(350,350))
imgCropped = img[0:200, 200:500]

cv2.imshow("Original Image",img)
cv2.imshow("Resize Image",imgResize)
cv2.imshow("Crop Image",imgCropped)
cv2.waitKey(0)