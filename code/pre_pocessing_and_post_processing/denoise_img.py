import numpy as np
import cv2 as cv

name = input("image: ")
img = cv.imread(name)
dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,35)
cv.imwrite('denoised.jpg', dst)