import cv2
from cv2 import waitKey
from cv2 import CV_8UC3
import numpy as np
src=cv2.imread("D:\\Document\\pictures\\test7.jpg",1)
srcgray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
dst=cv2.Canny(srcgray,50,100)
cv2.imshow("dst",dst)
#Laplacian算子，二阶偏导之和
dst_l=cv2.Laplacian(srcgray,CV_8UC3,dst,3,0.1)
cv2.imshow("dst_l",dst_l)
cv2.waitKey(0)