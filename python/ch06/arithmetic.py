import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


src1 = cv.imread('lenna256.bmp', cv.IMREAD_GRAYSCALE)
src2 = cv.imread('square.bmp', cv.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    exit()

dst1 = cv.add(src1, src2)
dst2 = cv.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst3 = cv.subtract(src1, src2)
dst4 = cv.absdiff(src1, src2)

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addWeighted')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
plt.show()
