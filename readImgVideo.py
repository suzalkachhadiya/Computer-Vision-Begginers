import cv2

# img=cv2.imread("coca7.jpg")

# cv2.imshow("coc",img)

# cv2.waitKey(0)

frameWidth=640
frameHieght=300

cap=cv2.VideoCapture("WhatsApp Video 2024-06-21 at 21.03.16_ce3add8b.mp4")

while True:
    success,img=cap.read()
    img=cv2.resize(img,(frameWidth,frameHieght))
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break