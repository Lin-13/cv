import imp
import cv2
from cv2 import THRESH_BINARY
from cv2 import GaussianBlur
from cv2 import WINDOW_NORMAL
import numpy as np
src=cv2.imread("D:\\Document\\pictures\\test3.jpg",1)
srcgray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
srcgray=cv2.GaussianBlur(srcgray,[3,3],1)
srccanny=cv2.Canny(srcgray,60,150)
ret,srcthreshod=cv2.threshold(srccanny,20,255,THRESH_BINARY)
src_contours,src_hierachy=cv2.findContours(srcthreshod,mode=cv2.RETR_LIST,method=cv2.CHAIN_APPROX_NONE,offset=[0,0])
print("contours")
print(src_contours)
print("histatchy")
print(src_hierachy)
dst=cv2.drawContours(src,src_contours,-1,[255,255,255],hierarchy=src_hierachy)
dst=cv2.drawContours(src,src_contours,-1,[0,0,255])
cv2.namedWindow("dst",WINDOW_NORMAL)
cv2.imshow("dst",dst)
print(src.shape)
cv2.waitKey(0)