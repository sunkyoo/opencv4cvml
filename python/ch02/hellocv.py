import numpy as np
import cv2

print('Hello OpenCV', cv2.__version__)

img = cv2.imread('lenna.bmp')

if img is None:
    print('Image load failed!')
    exit()

cv2.imshow('image', img)
cv2.waitKey()
