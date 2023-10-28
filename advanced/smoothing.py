import cv2 as cv

# We smooth an image when it tends to have alot of noise
# noise that's caused from camera sensors or lighting when the image was take

# Can reduce the noise using blurring methods
# Gaussian blurring, one of the most popular
# kernel size: window => (rows x columns)

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

# Method of blurring: averaging
# the bigger the kernel window, the more the blur
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian blur
# less blur compared to averaging 
gauss = cv.GaussianBlur(img, (7,7),0)
cv.imshow('Gaussian Blur', gauss)

# Median blur
# similar to averaging, instead of finding the average
# we find the median in the surrounding pixels 
median = cv.medianBlur(img,7)
cv.imshow('Median Blur', median)

# Bilateral blurring
# retains the edges in the image
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)