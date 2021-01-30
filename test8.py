import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread("C:\\opencv\\test.jpg", 1)
b = cv2.imread("C:\\opencv\\test.jpg", 1)  # b通道
e1 = cv2.getTickCount()
img1 = b[200:800, 300:1000]
img2 = b[150:750, 150:850]
dst = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)   ##############
b[150:750, 150:850] = dst
e2 = cv2.getTickCount()
t = (e2-e1) / cv2.getTickFrequency()
print(t)
cv2.namedWindow("test", cv2.WINDOW_NORMAL)
cv2.imshow("test", img)
cv2.imshow("b", b)

cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(b)
# plt.xticks([]), plt.yticks([])
# plt.show()
