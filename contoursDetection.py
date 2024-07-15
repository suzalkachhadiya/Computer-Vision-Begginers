import cv2
import numpy as np
from utils import stackImages, empty


frameWidth=1000
frameHieght=700

cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHieght)

cv2.namedWindow("parameters")
cv2.resizeWindow("parameters",640,240)
cv2.createTrackbar("threshold1","parameters",150,255,empty)
cv2.createTrackbar("threshold2","parameters",255,255,empty)
cv2.createTrackbar("Area","parameters",5000,3000,empty)

def getContours(img,imgContour):
    contours, hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContour,contours,-1,(255,0,255),7)

    for count in contours:
        area=cv2.contourArea(count)
        if area>1000:
            cv2.drawContours(imgContour,count,-1,(255,0,255),7)
            peri=cv2.arcLength(count,True)
            approx=cv2.approxPolyDP(count,0.02*peri,True)
            print(len(approx))

            x_, y_, w_, h_=cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x_,y_),(x_+w_,y_+h_),(0,255,0),5)
            cv2.putText(imgContour,"points:"+str(len(approx)),(x_+w_+20,y_+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
            cv2.putText(imgContour,"Area:"+str(int(area)),(x_+w_+20,y_+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)


while True:
    success,img=cap.read()
    imgContour=img.copy()

    imgBlur=cv2.GaussianBlur(img,(7,7),1)
    imgGray=cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)
    
    threshold1=cv2.getTrackbarPos("threshold1","parameters")
    threshold2=cv2.getTrackbarPos("threshold2","parameters")
    imgCanny=cv2.Canny(imgGray,threshold1,threshold2)
    kernel=np.ones((5,5))
    imgDil=cv2.dilate(imgCanny,kernel,iterations=1)

    getContours(imgDil,imgContour)

    imgStack=stackImages(0.5,([img,imgGray,imgCanny],
                              [imgDil,imgContour,imgContour]))

    cv2.imshow("result",imgStack)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break