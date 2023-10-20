import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')

# Three color channel => BGR
# cv.imshow('Cat',img)

# Converting to grayscale
# Only see the intensity distribution of pixels rather than the color
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# cv.imshow('Gray scale',gray)


# Blur an image
# 2nd parameter is kernel size, should be an odd number
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)
# cv.imshow('Blurred',blur)

img2 = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Original',img2)

# Edge Cascade: trying to find edges that are present in the image
# Reduce the edges by blurring the image
# Canny edge
canny = cv.Canny(img2, 125,175)
cv.imshow('Canny edge', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3),iterations=1)
cv.imshow('Dilated',dilated)

# Eroding 
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)

# Resize
# By default, interpolation=cv.INTER_AREA
# For enlarging, cv.INTER_LINEAR, cv.INTER_CUBIC
resized = cv.resize(img2, (500,500))
cv.imshow('Resized',resized)


# Cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)

