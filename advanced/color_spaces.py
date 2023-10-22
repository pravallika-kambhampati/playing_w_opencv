# how to switch between color spaces using opencv
# A color space is basically a space of colors, a system of representing
# an array of pixel colors

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/group 2.jpg')
cv.imshow('Original', img)

# you'd see an inversion of colors as matplotlib expects RGB order
plt.imshow(img)
plt.show()

# BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale',gray)

# BGR to HSV (hue, saturation, value)
# based on how humns think and conceive a color
# HSV separates the chromatic information (hue and saturation) from the brightness information (value).
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv) 

# BGR to LAB colorspace
# LAB color space is designed to be device-independent. 
# It is based on human vision and perceptual uniformity, meaning that the perceptual difference between colors is uniform across the color space. 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

"""
OpenCV reads images in BGR format
It is not the current system to represent colors outside of openCV
Outside of OpenCV -> RGB format
When trying to see img outside of openCV in any other python library like matplotlib
we'd see it an inversion of colors as it expects RGB order
Red -> Blue, Blue -> Red, hence convert!
"""

# BGR to RGB in opencv
rgb = cv.cvtColor(img,  cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# diplaying the converted rgb (from bgr) in matplotlib (get proper original image)
plt.imshow(rgb)
plt.show()

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

# Can't convert grayscale to HSV
# gotta convert grayscale to BGR, then BGR to HSV

cv.waitKey(0) 