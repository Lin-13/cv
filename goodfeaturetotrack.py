import numpy as np
import cv2
src0=cv2.imread("D:\\Document\\pictures\\test3.jpg",1)
src=cv2.cvtColor(src0,cv2.COLOR_BGR2GRAY)
srccp=src0.copy()
#监测角点
corner=cv2.goodFeaturesToTrack(src,200,0.01,10,useHarrisDetector=False)
print(corner)
print(corner.shape)
#绘制角点
corner=np.ceil(corner).astype(int)
for i in range(corner.shape[0]):
    cv2.circle(srccp,(corner[i][0][0],corner[i][0][1]),5,(0,255,255),-1)
cv2.namedWindow("dst",cv2.WINDOW_NORMAL)
cv2.imshow("dst",srccp)
cv2.waitKey(0)