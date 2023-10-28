import cv2 as cv
import numpy as np
# Masking allows us to focus on certain parts of an image that we'd like to focus on

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# size of mask should be same dimensions of the image 
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked image', masked)

cv.waitKey(0)