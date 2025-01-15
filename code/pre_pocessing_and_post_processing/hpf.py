import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = input("Enter filename to apply hpf filter: ")

img = cv2.imread(filename, 0)
height, width = img.shape

plt.figure("Input")
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

fft = np.log(np.abs(np.fft.fftshift(np.fft.fft2(img))))
plt.subplot(222),plt.imshow(fft, cmap = 'gray')
plt.title('Fourier Transform'), plt.xticks([]), plt.yticks([])

r = int(input("Enter radius for HPF. ex:20: ")) # 30
h_Filter_Low_Pass = np.zeros(img.size, img.dtype).reshape(img.shape)
for icounter in range(1, height):
    for jcounter in range(1, width):
        if ((height/2-icounter)**2 + (width/2 - jcounter)**2)**0.5 > r:
            h_Filter_Low_Pass[icounter, jcounter] = 1
plt.subplot(223),plt.imshow(h_Filter_Low_Pass, cmap = 'gray')
plt.title('Filter'), plt.xticks([]), plt.yticks([])

h_fft = (np.abs(np.fft.fftshift(np.fft.fft2(h_Filter_Low_Pass)))+1)
plt.subplot(224),plt.imshow(h_fft, cmap = 'gray')
plt.title('Fourier Transform (Filter)'), plt.xticks([]), plt.yticks([])

plt.figure("output")
img_color = cv2.imread(filename)
b,g,r = cv2.split(img_color)
def g_ifft(x):
    fshift = np.fft.fftshift(np.fft.fft2(x))
    new = fshift * (h_Filter_Low_Pass)
    g_ifft1 = (np.abs(np.fft.ifft2(np.fft.ifftshift(new)).real))
    g_ifft1 = cv2.normalize(g_ifft1,None,0,255,cv2.NORM_MINMAX, cv2.CV_8U)
    return g_ifft1
b,g,r = map(g_ifft, (b,g,r))
g_ifft1 = cv2.merge((b,g,r))

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)
# Do log transformation
c = 255 / np.log(1 + np.max(g_ifft1))
log_image = c * (np.log(g_ifft1 + 1))
log_image = np.array(log_image, dtype = np.uint8)

# Do gamma transformation
gamma_image = adjust_gamma(g_ifft1)

cv2.imwrite("gamma.jpg", gamma_image)
cv2.imwrite("log.jpg", log_image)
cv2.imwrite("style_hpf.jpg", g_ifft1)
g_ifft1 = cv2.cvtColor(g_ifft1, cv2.COLOR_BGR2RGB)

plt.subplot(),plt.imshow(g_ifft1)




plt.title('output'), plt.xticks([]), plt.yticks([])
plt.show()
