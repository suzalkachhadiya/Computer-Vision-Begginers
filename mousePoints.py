import cv2
import numpy as  np

circles=np.zeros((4,2),np.int32)
count=0

def mousePoints(event, x, y, flags, params):
    global count
    if event ==cv2.EVENT_LBUTTONDOWN:
        # print(x,y)
        circles[count]=x,y
        count=count+1

img=cv2.imread("images.jpeg")
img=cv2.resize(img,(500,400))

while True:
    width, height = 250, 350

    if count==4:
        pts1=np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
        # print(pts1)

        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput=cv2.warpPerspective(img,matrix,(width,height))

        cv2.imshow("output image",imgOutput)

    for x in range(0,4):
        cv2.circle(img,(int(circles[x][0]),int(circles[x][1])),3,(0,0,255),cv2.FILLED)

    cv2.imshow("original img",img)
    cv2.setMouseCallback("original img",mousePoints)
    cv2.waitKey(0)
