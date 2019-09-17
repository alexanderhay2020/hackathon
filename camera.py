# computer vision

import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(2) # reads from 2nd camera (cv2.VideoCapture(0) is the webcam)

# creates windows named "Stock" and "HSV"
cv2.namedWindow('Stock')
cv2.namedWindow('RGB')

# creates 6 trackbars in window HSV, hi/low thresholds
cv2.createTrackbar('rl','RGB',0,255,nothing) # (trackbar caption, parent window, preset val, max val,function called when trackbar moves)
cv2.createTrackbar('rh','RGB',0,255,nothing)
cv2.createTrackbar('gl','RGB',0,255,nothing)
cv2.createTrackbar('gh','RGB',0,255,nothing)
cv2.createTrackbar('bl','RGB',0,255,nothing)
cv2.createTrackbar('bh','RGB',0,255,nothing)

while True: # starts loop to run camera

    # Capture frame-by-frame
    ret, frame = cap.read() # returns value of the feed, the image itself

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts feed to grayscale
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) # converts feed to RGB

    # get current positions of four trackbars
    rl = cv2.getTrackbarPos('rl','RGB') # name of trackbar, name of parent window
    rh = cv2.getTrackbarPos('rh','RGB')
    gl = cv2.getTrackbarPos('gl','RGB')
    gh = cv2.getTrackbarPos('gh','RGB')
    bl = cv2.getTrackbarPos('bl','RGB')
    bh = cv2.getTrackbarPos('bh','RGB')

    rgbl = np.array([rl,gl,bl])
    rgbh = np.array([rh,gh,bh])

    mask = cv2.inRange(rgb, rgbl, rgbh)

    # Display the resulting frame
    #cv2.imshow('frame1',frame) # displays raw feed
    cv2.imshow('Stock',frame) # displays stock HSV feed
    cv2.imshow('RGB',mask) # displays modified HSV feed

    if cv2.waitKey(1) & 0xFF == ord('q'): # quits program if 'q' is pressed
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
