import sys
import numpy as np
import cv2


argc = len(sys.argv)
if argc < 3:
    print('Usage: stitching.exe <image_file1> <image_file2> [<image_file3> ...]')
    sys.exit()

imgs = []
for i in range(1, argc):
    img = cv2.imread(sys.argv[i])

    if img is None:
        print('Image load failed!')
        sys.exit()

    imgs.append(img)

stitcher = cv2.Stitcher_create()
status, dst = stitcher.stitch(imgs)

if status != cv2.Stitcher_OK:
    print('Error on stitching!')
    sys.exit()

cv2.imwrite('result.jpg', dst)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
