# OpenCV allows you to take an image and split it into different channels
# like blue, green and red components 

import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2],dtype='uint8')

# splitting the color channels
b,g,r = cv.split(img)

# displayed as grayscale images that show the distribution of pixel intensities
# lighter meaning far more concentration of those pixels
# darker shows little no pixels in that region
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape)
print(b.shape)
print(g.shape) 
print(r.shape)

# showing the actual colors, not in grayscale
blue = cv.merge([b,blank,blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank,blank,r])

cv.imshow('color_blue',blue)
cv.imshow('color_green',green)
cv.imshow('color_red',red)


# merging the color channels
merged = cv.merge([b,g,r])
cv.imshow('Merged image', merged)

cv.waitKey(0)