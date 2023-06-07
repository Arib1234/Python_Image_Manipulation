import cv2
old_img = cv2.imread("IMG.jpg")
old_img = cv2.resize(old_img,(400,400))

new_img = cv2.circle(img = old_img , center = (100,100), radius =50, color = (0,255,0), thickness=4 , lineType=16)
new_img = cv2.circle(img = old_img , center = (120,120), radius =80, color = (0,255,0), thickness=4 , lineType=16)

cv2.imshow("wscube",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()