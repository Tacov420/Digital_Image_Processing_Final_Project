import numpy as np
import cv2 as cv

name = input("image: ")
img = cv.imread(name)
dst = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
res = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
cv.imwrite('grayscale.jpg', res)