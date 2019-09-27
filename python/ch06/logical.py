import numpy as np
import cv2
from matplotlib import pyplot as plt


src1 = cv2.imread('lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    exit()

dst1 = cv2.bitwise_and(src1, src2)
dst2 = cv2.bitwise_or(src1, src2)
dst3 = cv2.bitwise_xor(src1, src2)
dst4 = cv2.bitwise_not(src1)

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('bitwise_and')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('bitwise_or')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('bitwise_xor')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('bitwise_not')
plt.show()
