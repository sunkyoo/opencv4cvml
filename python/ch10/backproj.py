import numpy as np
import cv2 as cv


# Calculate CrCb histogram from a reference image

ref = cv.imread('ref.png', cv.IMREAD_COLOR)
mask = cv.imread('mask.bmp', cv.IMREAD_GRAYSCALE)
ref_ycrcb = cv.cvtColor(ref, cv.COLOR_BGR2YCrCb)

channels = [1, 2]
cr_bins = 128
cb_bins = 128
histSize = [cr_bins, cb_bins]
cr_range = [0, 256]
cb_range = [0, 256]
ranges = cr_range + cb_range

hist = cv.calcHist([ref_ycrcb], channels, mask, histSize, ranges)

# Apply histogram backprojection to an input image

src = cv.imread('kids.png', cv.IMREAD_COLOR)
src_ycrcb = cv.cvtColor(src, cv.COLOR_BGR2YCrCb)

backproj = cv.calcBackProject([src_ycrcb], channels, hist, ranges, 1)

cv.imshow('src', src)
cv.imshow('backproj', backproj)
cv.waitKey()
cv.destroyAllWindows()
