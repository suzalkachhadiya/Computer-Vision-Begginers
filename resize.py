import cv2

path="360_F_81268225_eVHynMTlVQf3wVdYOoUEz8d8KolhVZm0.jpg"

img=cv2.imread(path)
print(img.shape)

width, height =500,500
imgResize=cv2.resize(img,(width,height))
print(imgResize.shape)

imgCropped=img[0:400,235:285]
imgCropResize=cv2.resize(imgCropped,(img.shape[1],img.shape[0]))
print(imgCropped.shape)

cv2.imshow("coc",img)
# cv2.imshow("cocR",imgResize)
cv2.imshow("cocC",imgCropped)
cv2.imshow("cocCR",imgCropResize)

cv2.waitKey(0)