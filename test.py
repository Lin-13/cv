from ctypes import pointer
from cv2 import EVENT_LBUTTONDBLCLK, EVENT_LBUTTONDOWN, WINDOW_AUTOSIZE, circle
import cv2
import numpy as np
point=[]
rect=[]
cnt=0
def mouse(event,x,y,flags,a):
    if event==EVENT_LBUTTONDBLCLK:
        global bg,point,rect,cnt
        bg[x,y]=[0,0,0]
        print("x={},y={}".format(x,y))
        point.append([x,y])
        nppoint=np.asarray(point)
        cnt=cnt+1
        if cnt>=2:
            rect=cv2.minAreaRect(nppoint)
            cv2.rectangle(bg,np.array(rect[0],dtype=int),np.array(rect[1],dtype=int),(0,0,255),-1)
            cv2.imshow("background",bg)
            cv2.rotatedRectangleIntersection()

#bg=np.array([255,255,255],dtype=np.uint8,ndmin=3)
bg=np.ones([600,1800],dtype=np.uint8)
bg=bg.reshape([600,600,3])
bg=bg*255
cv2.namedWindow("background",WINDOW_AUTOSIZE)
cv2.imshow("background",bg)
print(bg.shape)
cv2.setMouseCallback("background",mouse)
cv2.waitKey(0)
print("point")
print(point)
print("rect")
print(rect)