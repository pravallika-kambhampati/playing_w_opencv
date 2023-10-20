import cv2 as cv
import numpy as np


# dtype = uint8 refers to unsigned 8-bit, meaning values range from 0 to 255 (pixel range) => data type of an image
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank image',blank)

# color channels order BGR blue,green,red

# Paint the image a certain color
blank[:] = 255,255,255
# cv.imshow('Green',blank)

# blank[200:300,300:400] = 0,0,255
cv.imshow('Red with Green',blank)


# Drawing a rectangle
# thickness = cv.FILLED or thickness = -1  to fill in the shapes
cv.rectangle(blank,(0,0),(300,250),(0,0,0),thickness=3)
cv.imshow('Rectangle',blank)    

# Drawing a circle
blank = np.zeros((500,500,3),dtype='uint8')
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2),40, (0,0,255),thickness=cv.FILLED)
cv.imshow('Red Circle',blank)


# Drawing a line
cv.line(blank,(250,250),(450,250),(100,100,100),thickness=2)
cv.imshow('line with weird color',blank)


blank = np.zeros((500,500,3),dtype='uint8')
blank[:] = 255,255,255
# Write text
cv.putText(blank,'Hello World', (225,225), cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,0),thickness=2)
cv.imshow('Text Image',blank)


cv.waitKey(0)