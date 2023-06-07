import cv2
image = cv2.imread("IMG12.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
haar_face_cascade = cv2.CascadeClassifier("C:\\Users\Arib Lokhandwala\\Downloads\\raw.githubusercontent.com_opencv_opencv_4.x_data_haarcascades_haarcascade_frontalface_default.xml")
face = haar_face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors = 5)

for x,y,w,h in face:
    cv2.rectangle(image, (x,y), (x+w, y+h),(255,0,0),5)

print("Faces Found",len(face))
cv2.imshow("Face Detection",image)

cv2.imshow("Gray",gray)

cv2.waitKey(0)
cv2.destroyAllWindows()