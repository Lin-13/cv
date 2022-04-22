import cv2
from cv2 import COLOR_BGR2GRAY
from cv2 import WINDOW_NORMAL
from cv2 import MORPH_OPEN
from cv2 import MORPH_RECT
from cv2 import MORPH_ERODE
from cv2 import MORPH_DILATE
import numpy as np
src=cv2.imread("D:\\Document\\pictures\\test9.jpg",1)
src=cv2.pyrDown(src)
src=cv2.pyrDown(src)

srcgray=cv2.cvtColor(src,COLOR_BGR2GRAY)
#[s,srcgray,src]=cv2.split(src)
kernel=cv2.getStructuringElement(MORPH_RECT,[5,5])
#srcgray=cv2.morphologyEx(srcgray,MORPH_DILATE,kernel)
#blur
#srcgray=cv2.GaussianBlur(srcgray,[5,5],5)
srcgray=cv2.medianBlur(srcgray,3)
#srcgray=cv2.bilateralFilter(src,5,10,5)
#srcgray=cv2.blur(srcgray,[5,5])
#srcgray=cv2.equalizeHist(srcgray)
srcgray=cv2.Canny(srcgray,30,70)
#find line
dst=np.array([])
dst=cv2.HoughLinesP(srcgray,1,1*np.pi/180,100,np.array([]),50,50)
print(dst)
print(dst.shape)
#draw
#houghlinesp
for x in dst:
    x=x[0]
    cv2.line(src,np.array([x[0],x[1]]),np.array([x[2],x[3]]),[0,0,255],1,cv2.LINE_AA)
'''
for x in dst:
    x=x[0]
    if x[1]!=0.0:
        point1=np.array([0,int(x[0]/np.sin(x[1]/180*np.pi))])
        point2=np.array([int(x[0]/np.sin(x[1]/180*np.pi)),0])
        cv2.line(src,point1,point2,[0,0,255])
'''
#print
cv2.namedWindow("src",WINDOW_NORMAL)
cv2.imshow("src",src)
cv2.namedWindow("srcgray",WINDOW_NORMAL)
cv2.imshow("srcgray",srcgray)
cv2.waitKey(0)
print(src.shape)
print(srcgray.shape)
cv2.destroyAllWindows()
