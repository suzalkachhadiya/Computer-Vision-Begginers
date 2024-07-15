import cv2
import numpy as np

img=cv2.imread("images.jpeg")

width, height = 250, 350

pts1=np.float32([[180,2],[279,17],[102,103],[228,145]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
# print(pts1)

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

for x in range(0,4):
    cv2.circle(img,(int(pts1[x][0]),int(pts1[x][1])),3,(0,0,255),cv2.FILLED)

cv2.imshow("orginal image",img)
cv2.imshow("output image",imgOutput)

cv2.waitKey(0)