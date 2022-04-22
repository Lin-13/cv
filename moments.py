from cv2 import CHAIN_APPROX_NONE, COLOR_BGR2GRAY, CONTOURS_MATCH_I1, MORPH_BLACKHAT, MORPH_ERODE, MORPH_OPEN, MORPH_RECT, THRESH_BINARY_INV, WINDOW_AUTOSIZE, WINDOW_NORMAL, namedWindow, waitKey
import numpy as np
import cv2
src=cv2.imread("D:\\Document\\pictures\\testmoments2.jpg",1)
src=cv2.pyrDown(src)
namedWindow("src",WINDOW_NORMAL)
namedWindow("canny",WINDOW_NORMAL)

srcgray=cv2.cvtColor(src,COLOR_BGR2GRAY)
srcgray=cv2.GaussianBlur(srcgray,[3,3],3)
ele=cv2.getStructuringElement(MORPH_RECT,[3,3],[-1,-1])
srcgray=cv2.morphologyEx(srcgray,MORPH_ERODE,ele)
srcgray=cv2.equalizeHist(srcgray)

cv2.imshow("src",srcgray)
srccan=cv2.Canny(src,20,50)
line=cv2.HoughLinesP(srccan,1,5*np.pi/180,100,np.array([]),100,50)
line=np.asarray(line)
print(line)
print(line.shape)
#con,hie=cv2.findContours(srccan,cv2.RETR_LIST,CHAIN_APPROX_NONE)
#print(np.size(con),np.size(hie))
cv2.imshow("canny",srccan)
#srcbin=cv2.threshold(srcgray,50,255,THRESH_BINARY_INV)
#cv2.imshow("bin",srcbin)
waitKey(0)
cv2.imwrite("D:\\Document\\pictures\\testmoments1.jpg",src)