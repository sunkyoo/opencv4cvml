import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


src1 = cv.imread('lenna256.bmp', cv.IMREAD_GRAYSCALE)
src2 = cv.imread('square.bmp', cv.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    exit()

dst1 = cv.bitwise_and(src1, src2)
dst2 = cv.bitwise_or(src1, src2)
dst3 = cv.bitwise_xor(src1, src2)
dst4 = cv.bitwise_not(src1)

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('bitwise_and')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('bitwise_or')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('bitwise_xor')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('bitwise_not')
plt.show()
