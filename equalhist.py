import cv2
from cv2 import COLOR_BGR2GRAY
import numpy as np
src=cv2.imread("D:\\Document\\pictures\\test3.jpg",1)
srcgray=cv2.cvtColor(src,COLOR_BGR2GRAY)
dst=cv2.equalizeHist(srcgray)
cv2.imshow("src",srcgray)
cv2.imshow("dst",dst)
cv2.waitKey(0)
