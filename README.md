# 这是关于opencv特征检测的测试代码

由于部分原因，部分代码（主要是关于SIFT、SUFT算法）需要将opencv版本回退至3.4.1之前，python版本回退至3.6之前。

'''python
    sift=cv2.xfeather.SIFT.create()
    kp,des=sift.detectAndCompute(img,None)
    img=cv2.drawKeypoints(img,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
'''
