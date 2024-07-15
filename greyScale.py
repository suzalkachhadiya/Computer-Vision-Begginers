import cv2
import numpy as np

kernel =np.ones((5,5),np.uint8)
print(kernel)

path="coca7.jpg"

img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(15,15),0)
imgCanny=cv2.Canny(imgBlur,50,50)
imgDilation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("ex",img)
cv2.imshow("ex1",imgGray)
cv2.imshow("ex2",imgBlur)
cv2.imshow("ex3",imgCanny)
cv2.imshow("ex4",imgDilation)
cv2.imshow("ex5",imgEroded)

cv2.waitKey(0)