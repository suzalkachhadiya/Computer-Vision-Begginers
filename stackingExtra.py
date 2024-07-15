import cv2
import numpy as np
import utils

kernel =np.ones((5,5),np.uint8)
print(kernel)

path="Lenna_(test_image).png"

frameWidth=640
frameHieght=300

cap=cv2.VideoCapture(0)

while True:
    success,img=cap.read()
    img=cv2.resize(img,(frameWidth,frameHieght))
    # cv2.imshow("video",img)

    # img=cv2.imread(path)
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
    imgCanny=cv2.Canny(imgBlur,50,200)
    imgDilation=cv2.dilate(imgCanny,kernel,iterations=2)
    imgEroded=cv2.erode(imgDilation,kernel,iterations=1)
    imgBlank=np.zeros((200,200),np.uint8)

    # scale=0.8
    # img=cv2.resize(img,(0,0),None,scale,scale)
    # imgGray=cv2.resize(imgGray,(0,0),None,scale,scale)
    # imgBlur=cv2.resize(imgBlur,(0,0),None,scale,scale)
    # imgCanny=cv2.resize(imgCanny,(0,0),None,scale,scale)
    # imgDilation=cv2.resize(imgDilation,(0,0),None,scale,scale)
    # imgEroded=cv2.resize(imgEroded,(0,0),None,scale,scale)

    # imgGray=cv2.cvtColor(imgGray,cv2.COLOR_GRAY2BGR)
    # imgBlur=cv2.cvtColor(imgBlur,cv2.COLOR_GRAY2BGR)
    # imgCanny=cv2.cvtColor(imgCanny,cv2.COLOR_GRAY2BGR)
    # imgDilation=cv2.cvtColor(imgDilation,cv2.COLOR_GRAY2BGR)
    # imgEroded=cv2.cvtColor(imgEroded,cv2.COLOR_GRAY2BGR)

    # hor1=np.hstack((img,imgGray,imgBlur))
    # hor2=np.hstack((imgCanny,imgDilation,imgEroded))

    # ver=np.vstack((hor1,hor2))
    # width, height =800,500
    # ver=cv2.resize(ver,(width,height))

    # cv2.imshow("ex",img)
    # cv2.imshow("ex1",imgGray)
    # cv2.imshow("ex2",imgBlur)
    # cv2.imshow("ex3",imgCanny)
    # cv2.imshow("ex4",imgDilation)
    # cv2.imshow("ex5",imgEroded)
    # cv2.imshow("vertical",ver)

    stackedImages=utils.stackImages(0.2,([img,imgGray,imgBlur,imgCanny,imgDilation,imgEroded],
                                        #  [imgEroded,imgDilation,imgCanny,imgBlur,imgGray,img],
                                         [img,imgGray,imgBlur,imgCanny,imgDilation,imgEroded],
                                         [img,imgGray,imgBlur,imgCanny,imgDilation,imgEroded],
                                         [img,imgGray,imgBlur,imgCanny,imgDilation,imgEroded],
                                         [img,imgGray,imgBlur,imgCanny,imgDilation,imgEroded],
                                         [img,imgGray,imgBlur,imgCanny,imgDilation,imgEroded],
                                         [img,imgGray,imgBlur,imgCanny,imgDilation,imgEroded],
                                         [img,imgGray,imgBlur,imgCanny,imgDilation,imgEroded],
                                         [img,imgGray,imgBlur,imgCanny,imgDilation,imgEroded],
                                         [img,imgGray,imgBlur,imgCanny,imgDilation,imgEroded],
                                         [img,imgGray,imgBlur,imgCanny,imgDilation,imgEroded]
                                        ))
                                        #  [imgCanny,imgDilation,imgEroded]))

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    cv2.imshow("stacked images",stackedImages)
    # cv2.waitKey(0)