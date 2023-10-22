# Contours are basically the boundaries of obects, the line or curve that joins
# the continuous points along the boundary of an object. 

# Not the same as edges

import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)

# or threshold! 
# attempts to binarize an image 
# if the pixel density < 125, then the pixel will be set to 0 or black, if above 125 then it is set to white
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# pass thresh instead of canny

cv.imshow('Thresholded image',thresh)

# findContours looks at the edges, returns contours and hierarchies (hierarchical representation of all the contours)
# cv.RETR_LIST : returns all the contours 
# cv.RETR_EXTERNAL : returns all the external contours (outisde)
# cv.RETR_TREE : returns all the hierarchical contours present

# contour approximation method : how we want to approximate our contour
# cv.CHAIN_APPROX_NONE : does nothing, returns all the contours
# cv.CHAIN_APPROX_SIMPLE : compresses all the contours that are returned 
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# number of contours
print(f'{len(contours)} contour(s) found!')

# to reduce the number of contours blur the image :)


# visualizing the contours
cv.drawContours(blank,contours,-1, (0,0,255), 1)
cv.imshow('Contours Drawn',blank)



# Use canny method first, then find contours on that 
# rather than binarizing the image and finding contours on that (not most ideal as we're thresholding based on only one value)
cv.waitKey(0)