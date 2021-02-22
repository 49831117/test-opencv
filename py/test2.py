import cv2
import numpy as np

#mouse callback function
def draw_pic(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: # 滑鼠左鍵點兩下
        cv2.ellipse(img, (x, y), (20, 50), 45, 0, 180, (255, 0, 255), -1)

# 創建圖像與窗口並將窗口與回調函數綁定
img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_pic)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()
