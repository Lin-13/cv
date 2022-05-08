from cv2 import setMouseCallback
import numpy as np
import cv2
def callback(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print("x={},y={}".format(x,y))
        print("({},{},{})".format(src[y][x][0],src[y][x][1],src[y][x][2]))

src=cv2.imread("D:\\Document\\pictures\\testmoment1.jpg",1)
#src=src[1500:3000,1500:3000,:]
cv2.namedWindow("src",cv2.WINDOW_NORMAL)
cv2.imshow("src",src)
setMouseCallback("src",callback)
table=np.zeros((1,256,3),np.uint8)
print(src.shape)
print(table.shape)
bg_min= 100
for i in range(256):
    if i<bg_min:
        table[0][i]=[255,0,0]
src=cv2.LUT(src,table)

srcgray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
src_th=cv2.threshold(srcgray,10,255,cv2.THRESH_BINARY)[1]
edge=cv2.Canny(srcgray,3,5)

hierachy,r=cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(src,hierachy[1],-1,(0,255,0),3)
print(hierachy)
print(cv2.moments(src_th))
cv2.imshow("src",src)        
cv2.namedWindow("edge",cv2.WINDOW_NORMAL)
cv2.imshow("edge",edge)
cv2.waitKey(0)