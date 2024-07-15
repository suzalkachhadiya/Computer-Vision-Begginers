import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
print(img)

# img[100:200,50:100]=255, 0, 0

cv2.line(img,(img.shape[0],0),(0,img.shape[1]),(0,255,0),2)
cv2.rectangle(img,(200,100),(100,250),(0,0,255),cv2.FILLED)
cv2.circle(img,(300,300),40,(255,0,0),3)
cv2.putText(img,"Drow shapes",(75,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)
cv2.imshow("image",img)
cv2.waitKey(0)