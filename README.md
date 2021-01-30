# test-opencv
## Open CV
- [圖像插值演算法](http://www.1zlab.com/wiki/python-opencv-tutorial/opencv-interpolation-algrithm/)
- 影像處理
  - [線上資源 Teachable Machine](https://teachablemachine.withgoogle.com/)
  - [Lobe](https://lobe.ai/)

- 硬體：Coral TPU

- 終端機指令
  - `dir`
  - `tab`
  - `cd`
  - `copy`
  
- `pip install matplotlib`
  > 讀取時顏色不正常的原因之一：
  When the image file is read with the OpenCV function imread(), the order of colors is BGR (blue, green, red). On the other hand, in Pillow, the order of colors is assumed to be RGB (red, green, blue).
[source](https://note.nkmk.me/en/python-opencv-bgr-rgb-cvtcolor/)
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
- P.105 輪廓處理（算面積等）

- [人臉辨識](https://github.com/davisking/dlib-models)
  - shape_predictor_68_face_landmarks
    - 放進相同目錄，為一資料檔
        - 人臉特徵向量值


**Side Project**
  1. [點兩下滑鼠畫出傾斜 45 度半個實心橢圓](https://github.com/49831117/test-opencv/blob/main/test.py)
  2. canny 蝴蝶
  3. 抓取輪廓
  4. [人臉辨識](https://github.com/49831117/test-opencv/blob/main/test15.py)
 
