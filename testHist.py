from matplotlib import pyplot
import numpy as np
import cv2
src=cv2.imread("D:\\Document\\pictures\\cat.jpg",cv2.IMREAD_ANYCOLOR)
cv2.imshow("src",src)
#cv2.namedWindow("src",cv2.WINDOW_AUTOSIZE)

dst=np.zeros(src.shape)
dst1=cv2.GaussianBlur(src,[11,11],3,3,cv2.BORDER_DEFAULT)
#cv2.namedWindow("dst",cv2.WINDOW_AUTOSIZE)
histdst=cv2.equalizeHist(src)
cv2.imshow("dst",dst1)
[hist,bins]=np.histogram(src,bins=np.linspace(0,255,10,True))
print("hist={}".format(hist))
print("bins={}".format(bins))

pyplot.hist(np.ravel(src),bins)
pyplot.show()
cv2.waitKey(0)
print("id src {}".format(id(src)))
print("id dst {}".format(id(dst)))
np.save("src_cat",src)