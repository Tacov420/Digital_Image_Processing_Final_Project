import numpy as np
import cv2 as cv

name = input("image: ")
origin_img = cv.imread(name)

# 圖像歸一化，且轉換為浮點型
fImg = origin_img.astype(np.float32)
fImg = fImg / 255.0

# 顏色空間轉換 BGR -> HLS
hlsImg = cv.cvtColor(fImg, cv.COLOR_BGR2HLS)
hlsCopy = np.copy(hlsImg)

lightness = 0 # lightness 調整為  "1 +/- 幾 %"
saturation = 300 # saturation 調整為 "1 +/- 幾 %"

# 亮度調整
hlsCopy[:, :, 1] = (1 + lightness / 100.0) * hlsCopy[:, :, 1]
hlsCopy[:, :, 1][hlsCopy[:, :, 1] > 1] = 1  # 應該要介於 0~1，計算出來超過1 = 1

# 飽和度調整
hlsCopy[:, :, 2] = (1 + saturation / 100.0) * hlsCopy[:, :, 2]
hlsCopy[:, :, 2][hlsCopy[:, :, 2] > 1] = 1  # 應該要介於 0~1，計算出來超過1 = 1

# 顏色空間反轉換 HLS -> BGR 
result_img = cv.cvtColor(hlsCopy, cv.COLOR_HLS2BGR)
result_img = ((result_img * 255).astype(np.uint8))

cv.imwrite('saturated.jpg', result_img)