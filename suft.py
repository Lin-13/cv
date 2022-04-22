import numpy as np
import cv2
src=cv2.imread("D:\\Document\\pictures\\test3.jpg",1)
src=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
suft=cv2.xfeatures2d.SURF_create()
suft.setHessianThreshold(400)
suft.setNOctaves(4)
suft.setNOctaveLayers(2)
suft.setUpright(True)
kp,des=suft.detectAndCompute(src,None)
print(kp)
print(des)
src=cv2.drawKeypoints(src,kp,None,(0,255,0),4)
cv2.imshow("suft",src)
cv2.imwrite(".\\pictures\\suft.png",src)
cv2.waitKey(0)
