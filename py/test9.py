# p.57 顏色空間轉換
import cv2
flags=[i for i in dir(cv2) if i.startswith('COLOR_')]
print (flags)
cv2.cvtColor(img, cv2.COLOR_RGB2HSV) # 轉換顏色空間
