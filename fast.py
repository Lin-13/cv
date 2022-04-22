import cv2
import numpy as np
from matplotlib import pyplot as plt
src=cv2.imread("D:\\Document\\pictures\\test3.jpg",0)
#初始化fast类
fast=cv2.FastFeatureDetector_create()
#获取关键点
keypoint=fast.detect(src,None)
img=cv2.drawKeypoints(src,keypoint,None,color=(255,0,0))
#打印参数
print("threshold:",fast.getThreshold())
print("nonmaxSuppression:",fast.getNonmaxSuppression())
print("neighborhood:",fast.getType())
print("Total Keypoints with non max suppression:",len(keypoint))
#输出图像
cv2.imwrite("D:\\Document\\pictures\\fast.jpg",img)
cv2.namedWindow("fast",cv2.WINDOW_NORMAL)
cv2.imshow("fast",img)

#disable nonmaxSuppression
fast.setNonmaxSuppression(0)
keypoint=fast.detect(src,None)
img=cv2.drawKeypoints(src,keypoint,None,color=(255,0,0))
print("Total Keypoints without non max suppression:",len(keypoint))
cv2.imshow("fast1",img)
cv2.waitKey(0)