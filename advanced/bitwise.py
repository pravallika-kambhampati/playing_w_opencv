# bitwise operators: and, or, xor, not
# pixel off: 0, on: 1 

import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('My Rectangle', rectangle)
cv.imshow('My Circle', circle)
 
# Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# Bitwise OR
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR', bitwise_or)

dest = np.zeros((400,400), dtype='uint8')
# Bitwise NOT
bitwise_not = cv.bitwise_not(rectangle, dest)
cv.imshow('Bitwise NOT', bitwise_not)

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR', bitwise_xor)

cv.waitKey(0)


