import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread("test.jpg", 1)
b = cv2.imread("..\\test-opencv\\image\\test.jpg", 1)  # b通道
b[0:100, 30:350, 0] = 0       # 指定某區塊的通道顏色
b[50:60, 300:700, 1] = 0      # 指定全區域的通道顏色 eg. [:, :, 1]
b[0:500, 30:60, 2] = 0

plt.imshow(b)
plt.xticks([]), plt.yticks([])
plt.show()
