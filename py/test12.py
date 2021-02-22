# # 框出 bald_eagle.jpg 的輪廓
# rf：https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F5%2F59%2FBald_Eagle_-_%2522Helga%2522_-_Haliaeetus_leucocephalus2.jpg%2F220px-Bald_Eagle_-_%2522Helga%2522_-_Haliaeetus_leucocephalus2.jpg&imgrefurl=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E7%2599%25BD%25E9%25A0%25AD%25E6%25B5%25B7%25E9%25B5%25B0&tbnid=wuPmH9CS8yUGSM&vet=12ahUKEwiwwJ6j3MLuAhWTEKYKHRALDX0QMygBegUIARCmAQ..i&docid=_XCXu6ovsn1zmM&w=220&h=331&q=%E7%BE%8E%E5%9C%8B%E8%80%81%E9%B7%B9%20wiki&ved=2ahUKEwiwwJ6j3MLuAhWTEKYKHRALDX0QMygBegUIARCmAQ

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('..\\test-opencv\\image\\bald_eagle.jpg')
img1 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(imgray, (5, 5), 2, 1)
'''
高斯平滑
高斯濾波是一種線性平滑濾波，適用於消除高斯噪聲，
高斯濾波就是對整幅影象進行加權平均的過程，每一個畫素點的值，
都由其本身和鄰域內的其他畫素值經過加權平均後得到。

高斯濾波的具體操作是：
用一個模板（或稱卷積、掩模）掃描影象中的每一個畫素，用模板確定的鄰域內畫素的加權平均灰度值去替代模板中心畫素點的值。
高斯濾波後圖像被平滑的程度取決於標準差。
它的輸出是領域畫素的加權平均，同時離中心越近的畫素權重越高。
因此，相對於均值濾波（mean filter）它的平滑效果更柔和，而且邊緣保留的也更好。

平滑視窗小，對標準差的變化不敏感，平滑效果差別不大。
平滑視窗大，對標準差的變化很敏感，平滑效果差別很大。

cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) 
src: 影象矩陣 
ksize: 濾波視窗尺寸 ，高斯卷積大小且寬高均為奇數但可以不相等
sigmaX: 水平方向上的標準差
sigmaY: 垂直方向的標準差預設為0表示與水平方向相同

rf：https://www.itread01.com/content/1548728312.html
'''

edges = cv2.Canny(blurred, 12, 150)

'''
在作邊緣偵測時，通常會調整模糊參數(cv2.GaussianBlur)或邊緣檢測參數(cv2.Canny)來達到想要的結果

步驟大約分成

1. 影像轉灰階： cv2.cvtColor
2. 影像去雜訊： cv2.GaussianBlur
   cv2.GaussianBlur第二個參數是指定Gaussian kernel size，本範例使用5×5

邊緣偵測： cv2.Canny
採用雙門檻值
第二個參數是指定門檻值 threshold1 – first threshold for the hysteresis procedure.
第二個參數是指定門檻值 threshold2 – second threshold for the hysteresis procedure.

rf：https://shengyu7697.github.io/blog/2020/03/18/Python-OpenCV-canny/
'''
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
draw = cv2.drawContours(img1, contours, -1, (200, 200, 0), 2)

plt.subplot(131), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(132), plt.imshow(edges,cmap='gray'), plt.title('Edge Image')
plt.subplot(133), plt.imshow(cv2.cvtColor(draw,cv2.COLOR_BGR2RGB)), plt.title('contour Image')

plt.show()

############################

def nothing(x):
    pass

edges = cv2.Canny(img, 50, 100)   
cv2.namedWindow("image")
cv2.createTrackbar('minval', 'image', 0, 255, nothing)
cv2.createTrackbar('maxval', 'image', 0, 255, nothing)


while(1):
    cv2.imshow('image', edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    minval = cv2.getTrackbarPos('minval', 'image')
    maxval = cv2.getTrackbarPos('maxval', 'image')
    edges = cv2.Canny(img, minval, maxval)

############################




'''
Q：結合test11？
'''

'''
NOTE：https://chtseng.wordpress.com/2016/12/05/opencv-contour%E8%BC%AA%E5%BB%93/
'''
