import numpy as np
import cv2 as cv

name = input("video: ")
cap = cv.VideoCapture(name)
count = 0

frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
print("frames = %d" % len(frames))

dst = []
# Denoise frames considering all the frames
for i in range(len(frames)):
    print(i)
    blur_img = cv.GaussianBlur(frames[i], (0, 0), 50)
    dst.append(cv.addWeighted(frames[i], 1.5, blur_img, -0.5, 0))

frame_num = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('sharpened.mp4', fourcc, 30, (frame_width,frame_height))
for i in range(len(dst)):
    out.write(dst[i])
cap.release()
out.release()