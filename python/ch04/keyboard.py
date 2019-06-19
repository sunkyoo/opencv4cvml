import numpy as np
import cv2 as cv


img = cv.imread('lenna.bmp')

if img is None:
    print('Image load failed!')
    exit()

cv.namedWindow('img')
cv.imshow('img', img)

while True:
    keycode = cv.waitKey()
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv.imshow('img', img)
    elif keycode == 27 or keycode == ord('q') or keycode == ord('Q'):
        break

cv.destroyAllWindows()
