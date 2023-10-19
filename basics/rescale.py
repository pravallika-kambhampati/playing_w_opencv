# Resizing and Rescaling media
# Rescaling implies modifying the height and width to a particular height and weight to lessen the computational strain

import cv2 as cv

# Reading video and image
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
img = cv.imread('Resources/Photos/cat.jpg')


# Resizes the frame
# Can be used for photos, videos and live video
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# Can be used only for live video captured from webcam
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# Reading and displaying every frame of the video, both original and resized
while True:
    isTrue, frame = capture.read()
    resized_frame = rescaleFrame(frame)
  

    cv.imshow('Resized Video', resized_frame)
    cv.imshow('Original Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# Displaying original and resized photo
cv.imshow('Original Photo', img)

resized_cat = rescaleFrame(img, scale=0.2)
cv.imshow('Resized Photo',resized_cat)


cv.waitKey(0)
cv.destroyAllWindows()