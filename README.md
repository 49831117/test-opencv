# test-opencv
## Open CV

- 上課講義：https://sites.google.com/mail.cjcu.edu.tw/opencv/

- 網路資源
  - Teachable Machine：https://teachablemachine.withgoogle.com/

- 硬體：Coral TPU

- 終端機指令
  - `dir`
  - `tab`
  - `cd`
  - `copy`
  
- `pip install matplotlib`
  > 讀取時顏色不正常的原因之一：
  When the image file is read with the OpenCV function imread(), the order of colors is BGR (blue, green, red). On the other hand, in Pillow, the order of colors is assumed to be RGB (red, green, blue).
  source：https://note.nkmk.me/en/python-opencv-bgr-rgb-cvtcolor/
  - open cv 中為 BGR

- P.39
  - ROI：感興趣的區塊
- p.44
  - 通道?
- p.46
  - `add()` 跟 `+` 的差異
  - `cv2.addWeighted()`
- P.57
  - HSV @wiki
  - HSL @wiki
  - WSL1 vs WSL2 系統
- P.100 金字塔：將圖片融合
  - **[可逆?] 如果已知融合的圖、階數，能否找回原圖**  
- P.105 輪廓處理(算面積等)
  1. 滑鼠 點
  2. canny 蝴蝶
  3. 抓取輪廓
  4. 
 
