import numpy as np
import cv2 as cv

name = input("image: ")

img = cv.imread(name)
res = cv.GaussianBlur(img,(9,9),0)
cv.imwrite('smoothed.jpg', res)