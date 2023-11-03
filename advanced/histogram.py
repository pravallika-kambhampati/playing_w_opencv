import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Cats',img)

# Using histograms to visualize the distribution of pixel intensities in an image
# Can be constructed for either grayscale images or rgb images
blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.circle(blank,(img.shape[1]//2, img.shape[0]//2), 100,255, -1)
cv.imshow('Mask', mask) 

masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Masked image', masked)

# Grayscale histogram
# gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])
gray_hist = cv.calcHist([masked],[0],mask,[256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
# range of pixel intensities
plt.xlabel('Bins')
# number of pixels with the given intensity
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()



# Color Histogram
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show() 

cv.waitKey(0)