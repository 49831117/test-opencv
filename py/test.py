import cv2
import numpy as np
from matplotlib import pyplot as plt

# print(img)
# cv2.namedWindow('test', cv2.WINDOW_NORMAL)
# cv2.imshow("test", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE) # cv2.IMREAD_GRAYSCALE 黑白(1)
# img = cv2.imread('test.jpg',0)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic') # interpolation 內插植
# plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()


img = np.ones((512, 512, 3), np.uint8)
#Import only if not previously imported
# import cv2
# Coordinates must be a tuple - (x,y)
cv2.line(img,(500, 500),(0, 0),(255,0,0),5)                   #Color is by default black
# Coordinates must be a tuple - (x,y)
cv2.rectangle(img,(100, 100),(300, 300),(0,255,0),6)                   #Color is by default black
# for i in range(100, 300):
#     cv2.rectangle(img,(100+i, 100),(300+i, 300),(0,150,0),9)
# Coordinates must be a tuple - (x,y)
cv2.circle(img,(200, 200), 150, (100, 100, 100) , 2)                     #Color is by default black

points = np.array([[200, 200], [300, 100], [400, 200], [400, 400], [200, 400]])
cv2.polylines(img, [points], True, (0,0,100), 5)                   #Color is by default black


#Coordinates must be a tuple - (x,y)
cv2.ellipse(img,(256, 256),(100, 50), 0, 0, 180, (255, 255, 0), 3)                        #Color is by default black


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Open CV", (100, 100),font, 2, (0, 255, 255),5) 
# "text"不能輸入中文


# 跟滑鼠互動：搜尋 event






cv2.imshow("Window Name", img)
cv2.waitKey(0)
cv2.destroyAllWindows()