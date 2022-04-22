from ctypes import pointer
from cv2 import EVENT_LBUTTONDBLCLK, EVENT_LBUTTONDOWN, WINDOW_AUTOSIZE, circle
import cv2
import numpy as np
import sys
point=[]
rect=[]
cir=[]
cnt=0
def mouse(event,x,y,flags,a):
    if event==EVENT_LBUTTONDBLCLK:
        global bg,point,rect,cnt,cir
        bg[x,y]=[0,0,0]
        print("x={},y={}".format(x,y))
        point.append([x,y])
        nppoint=np.asarray(point)
        cnt=cnt+1
        ##circle(bg,np.array([x,y]),5,(0,0,0))#3.9版本
        cv2.circle(bg,(x,y),5,(0,0,0),-1)#python3.6版本
        if cnt>=2:
            '''
            rect=cv2.boundingRect(nppoint)
            cv2.rectangle(bg,np.array([rect[0],rect[1]]),np.array([rect[2],rect[3]]),(0,0,255),5)
            cv2.imshow("background",bg)
            print("point")
            print(nppoint)
            print("rect")
            print(rect)
            '''
            cir=cv2.minEnclosingCircle(nppoint)
            print(cir)
            cv2.circle(bg,np.array(cir[0],dtype=int),int(cir[1]),[0,0,255])
            print("point")
            print(nppoint)
            print("circle")
            print(cir)
        cv2.imshow("background",bg)

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
print(cir)