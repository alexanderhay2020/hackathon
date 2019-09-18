# computer vision

import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(2) # reads from 2nd camera (cv2.VideoCapture(0) is the webcam)
#img = cv2.imread('/path/to/file.xxx',0) # reads image from a file

# creates windows named "HSV". Name can be an str variable
cv2.namedWindow('HSV')

# creates 6 trackbars in window HSV, sets hi/low thresholds
cv2.createTrackbar('hl','HSV',0,255,nothing) # (trackbar caption, parent window, preset val, max val,function called when trackbar moves)
cv2.createTrackbar('hh','HSV',0,255,nothing)
cv2.createTrackbar('sl','HSV',0,255,nothing)
cv2.createTrackbar('sh','HSV',0,255,nothing)
cv2.createTrackbar('vl','HSV',0,255,nothing)
cv2.createTrackbar('vh','HSV',0,255,nothing)

def filter(img):

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # get current positions of four trackbars
    hl = cv2.getTrackbarPos('hl','HSV') # name of trackbar, name of parent window (both ban be variables w/ strings)
    hh = cv2.getTrackbarPos('hh','HSV')
    sl = cv2.getTrackbarPos('sl','HSV')
    sh = cv2.getTrackbarPos('sh','HSV')
    vl = cv2.getTrackbarPos('vl','HSV')
    vh = cv2.getTrackbarPos('vh','HSV')

    #hsvl = np.array([hl,sl,vl])
    hsvl = np.array([0,137,77])  # filter for red ball
    #hsvh = np.array([hh,sh,vh])
    hsvh = np.array([5,255,255])

    # applies threshold mask from hi/low HSV values
    mask = cv2.inRange(hsv, hsvl, hsvh)
    # applies Gaussian Blur
    blur = cv2.GaussianBlur(mask,(7,7),0)
    # applies mask to input img
    img=cv2.bitwise_and(img,img,mask=blur)
    # convert to grayscale
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    return img

while True: # starts loop to run camera

    # read current frame
    ret, frame = cap.read() # returns value of the feed, the image itself

    frame=filter(frame)
    cv2.imshow('HSV',frame) # displays image stored in hsv

    if cv2.waitKey(1) & 0xFF == ord('q'): # quits program if 'q' is pressed
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
