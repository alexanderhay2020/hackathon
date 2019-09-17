# computer vision

import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(2) # reads from 2nd camera (cv2.VideoCapture(0) is the webcam)

# creates windows named "Stock" and "HSV"
cv2.namedWindow('Stock')
cv2.namedWindow('HSV')

# creates 6 trackbars in window HSV, hi/low thresholds
cv2.createTrackbar('hh','HSV',0,255,nothing) # (trackbar caption, parent window, preset val, max val,function called when trackbar moves)
cv2.createTrackbar('hl','HSV',0,255,nothing)
cv2.createTrackbar('sh','HSV',0,255,nothing)
cv2.createTrackbar('sl','HSV',0,255,nothing)
cv2.createTrackbar('vh','HSV',0,255,nothing)
cv2.createTrackbar('vl','HSV',0,255,nothing)

while True: # starts loop to run camera

    # Capture frame-by-frame
    ret, frame = cap.read() # returns value of the feed, the image itself

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts feed to grayscale
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # converts feed to HSV

    # get current positions of four trackbars
    hl = cv2.getTrackbarPos('hl','HSV') # name of trackbar, name of parent window
    hh = cv2.getTrackbarPos('hh','HSV')
    sl = cv2.getTrackbarPos('sl','HSV')
    sh = cv2.getTrackbarPos('sh','HSV')
    vl = cv2.getTrackbarPos('vl','HSV')
    vh = cv2.getTrackbarPos('vh','HSV')

    hsvl = np.array([hl,sl,vl])
    hsvh = np.array([hh,sh,vh])

    mask = cv2.inRange(hsv, hsvl, hsvh)

    # Display the resulting frame
    #cv2.imshow('frame1',frame) # displays raw feed
    cv2.imshow('Stock',hsv) # displays stock HSV feed
    cv2.imshow('HSV',mask) # displays modified HSV feed

    if cv2.waitKey(1) & 0xFF == ord('q'): # quits program if 'q' is pressed
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
