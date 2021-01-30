import cv2
import numpy as np

cap=cv2.VideoCapture(0)

# Define the code and create VideoWriter object
fourcc = cv2.cv.FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))


# while(cap.isOpened()):  ###### 檢查攝影鏡頭是否開啟?
#     ret, frame = cap.read()
#     if ret==True:
#         frame = cv2.flip(frame,0)
#         # write the flipped frame
#         out.write(frame)
        
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#         else:
#             break

while(1):  
    # 獲取每一禎
    ret,frame = cap.read() 
    # 轉換到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 設定藍色的閾值
    lower_blue = np.array([50, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # 根據閾值構建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # 對原圖像和掩模進行位運算
    res = cv2.bitwise_and(frame, frame, mask = mask)
    # 顯示圖片
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows() # 關閉窗口