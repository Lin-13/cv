from cv2 import calcHist
import numpy as np
import cv2
import matplotlib.pyplot as plt
#RGB
#显示图像
src=cv2.imread("D:\\Document\\pictures\\test3.jpg",1)
cv2.namedWindow("src",cv2.WINDOW_NORMAL)
cv2.imshow("src",src)
src=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
#RGB
redhist=calcHist([src],[0],None,[256],[0,256])
greenhist=calcHist([src],[1],None,[256],[0,256])
bluehist=calcHist([src],[2],None,[256],[0,256])
#绘制直方图
plt.subplot(311)
plt.title("red")
plt.plot(redhist)
plt.subplot(312)
plt.title("green")
plt.plot(greenhist)
plt.subplot(313)
plt.title("blue")
plt.plot(bluehist)
plt.show()
#HSV
src=cv2.cvtColor(src,cv2.COLOR_RGB2HSV)
Hhist=calcHist([src],[0],None,[256],[0,256])
Shist=calcHist([src],[1],None,[180],[0,180])
Vhist=calcHist([src],[2],None,[180],[0,180])
plt.subplot(311)
plt.title("H")
plt.plot(Hhist)
plt.subplot(312)
plt.title("S")
plt.plot(Shist)
plt.subplot(313)
plt.title("V")
plt.plot(Vhist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
