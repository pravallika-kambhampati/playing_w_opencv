import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
# computes the gradient of the gray-scale image
# transition: black to white -> positive slope
# white to black -> negative slope 
lap =  cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F,1 ,0 )
sobely = cv.Sobel(gray, cv.CV_64F,0 ,1 )
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined sobel', combined_sobel)

# Canny: more advanced, multi-stage, uses sobel in one of the steps
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny',canny)

cv.waitKey(0) 