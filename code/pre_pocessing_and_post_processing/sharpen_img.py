import numpy as np
import cv2 as cv

name = input("image: ")

img = cv.imread(name)
blur_img = cv.GaussianBlur(img, (0, 0), 50)
res = cv.addWeighted(img, 1.5, blur_img, -0.5, 0)
cv.imwrite('sharpened.jpg', res)