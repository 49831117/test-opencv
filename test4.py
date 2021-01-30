import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("test.jpg", 1)
# print(img.shape, img.size)

roi = img[98:178, 954:1019]   # 聖誕樹上的星星 左上(954,98) & 右下(1019,178)
img[107:187, 459:524] = roi   # 移到屋頂上


img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.xticks([]), plt.yticks([])
plt.show()
