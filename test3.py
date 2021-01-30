# 用滑鼠調整 RGB 的數值，產出該顏色的圖。

import cv2
import numpy as np

def nothing(x):
    pass

# 先做一張黑色的圖
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
switch='0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
    if s == 0:
        img[:]=0  # 黑色為 0，若預設白色，改成 img[:] = [255, 255, 255]
    else:
        img[:]=[b,g,r]
cv2.destroyAllWindows()