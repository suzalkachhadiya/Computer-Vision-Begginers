import cv2
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

while True:
    success,img=cap.read()
    imgBlur=cv2.GaussianBlur(img,(7,7),1)
    imgGray=cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)
    
    threshold1=cv2.getTrackbarPos("threshold1","parameters")
    threshold2=cv2.getTrackbarPos("threshold2","parameters")
    imgCanny=cv2.Canny(imgGray,threshold1,threshold2)

    kernel=cv2.dilate(imgCanny,kernel,iterations=1)

    imgStack=stackImages(0.5,([img,imgGray,imgCanny]))

    cv2.imshow("result",imgStack)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break