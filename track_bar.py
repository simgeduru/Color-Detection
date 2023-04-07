import cv2
import numpy as np

img= np.zeros((512,512,3),np.uint8)

def nothing(x):
    pass

cv2.namedWindow("Resim")

cv2.createTrackbar("R","Resim",0,255,nothing)
cv2.createTrackbar("G","Resim", 0,255,nothing)
cv2.createTrackbar("B","Resim", 0,255,nothing)


while(True) :
    cv2.imshow("Resim",img)

    r=cv2.getTrackbarPos("R","Resim")
    g=cv2.getTrackbarPos("G","Resim")
    b=cv2.getTrackbarPos("B","Resim")

    img[10:100]= [b,g,r]

    if cv2.waitKey(1)& 0xFF==27:
        break
        #simge duru