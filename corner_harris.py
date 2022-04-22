import numpy as np
import cv2
src=cv2.imread("D:\\Document\\pictures\\test7.jpg",1)
cv2.namedWindow("src",cv2.WINDOW_NORMAL)
cv2.imshow("src",src)
src=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
corner=cv2.cornerHarris(src,2,3,0.04)
corner=cv2.threshold(corner,0.1*corner[1].max(),255,cv2.THRESH_BINARY)
cv2.namedWindow("dst",cv2.WINDOW_NORMAL)
print(corner)
cv2.imshow("dst",corner[1])
cv2.waitKey(0)