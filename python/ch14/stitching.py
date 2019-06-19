import numpy as np
import cv2 as cv
import sys


argc = len(sys.argv)
if argc < 3:
    print('Usage: stitching.exe <image_file1> <image_file2> [<image_file3> ...]')
    exit()

imgs = []
for i in range(1, argc):
    img = cv.imread(sys.argv[i])

    if img is None:
        print('Image load failed!')
        exit()

    imgs.append(img)

stitcher = cv.Stitcher_create()
status, dst = stitcher.stitch(imgs)

if status != cv.Stitcher_OK:
    print('Error on stitching!')
    exit()

cv.imwrite('result.jpg', dst)

cv.imshow('dst', dst)
cv.waitKey()
cv.destroyAllWindows()
