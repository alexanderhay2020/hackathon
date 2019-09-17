# computer vision

import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(2) # reads from 2nd camera (cv2.VideoCapture(0) is the webcam)

# creates window named "HSV"
cv2.namedWindow('HSV')

# creates 3 trackbars in window HSV
cv2.createTrackbar('H','HSV',0,255,nothing) # (trackbar caption, parent window, preset val, max val,function called when trackbar moves)
cv2.createTrackbar('S','HSV',0,255,nothing)
cv2.createTrackbar('V','HSV',0,255,nothing)

while True: # starts loop to run camera

    # Capture frame-by-frame
    ret, frame = cap.read() # returns value of the feed, the image itself

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts feed to grayscale
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # converts feed to HSV

    # Display the resulting frame
    #cv2.imshow('frame1',frame) # displays raw feed
    #cv2.imshow('frame2',gray) # displays grayscale feed
    cv2.imshow('HSV',hsv) # displays HSV feed


    # get current positions of four trackbars
    h = cv2.getTrackbarPos('H','HSV') # name of trackbar, name of parent window
    s = cv2.getTrackbarPos('S','HSV')
    v = cv2.getTrackbarPos('V','HSV')

    if cv2.waitKey(1) & 0xFF == ord('q'): # quits program if 'q' is pressed
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
