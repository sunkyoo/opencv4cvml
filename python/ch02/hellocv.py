import numpy as np
import cv2 as cv

print('Hello OpenCV', cv.__version__)

img = cv.imread('lenna.bmp')

if img is None:
    print('Image load failed!')
    exit()

cv.imshow('image', img)
cv.waitKey()
