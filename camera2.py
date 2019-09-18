# computer vision

import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(2) # reads from 2nd camera (cv2.VideoCapture(0) is the webcam)
#img = cv2.imread('/path/to/file.xxx',0) # reads image from a file

# creates windows named "Stock" and "HSV"
cv2.namedWindow('Stock')
cv2.namedWindow('HSV')
cv2.namedWindow('Blur')

# creates 6 trackbars in window HSV, hi/low thresholds
cv2.createTrackbar('hl','HSV',0,255,nothing) # (trackbar caption, parent window, preset val, max val,function called when trackbar moves)
cv2.createTrackbar('hh','HSV',0,255,nothing)
cv2.createTrackbar('sl','HSV',0,255,nothing)
cv2.createTrackbar('sh','HSV',0,255,nothing)
cv2.createTrackbar('vl','HSV',0,255,nothing)
cv2.createTrackbar('vh','HSV',0,255,nothing)
#cv2.createTrackbar('blur','Blur',10,100,nothing)

def filter(img):

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hl = cv2.getTrackbarPos('hl','HSV') # name of trackbar, name of parent window (both ban be variables w/ strings)
    hh = cv2.getTrackbarPos('hh','HSV')
    sl = cv2.getTrackbarPos('sl','HSV')
    sh = cv2.getTrackbarPos('sh','HSV')
    vl = cv2.getTrackbarPos('vl','HSV')
    vh = cv2.getTrackbarPos('vh','HSV')

    hsvl = np.array([hl,sl,vl])
    hsvh = np.array([hh,sh,vh])

    hsvl = np.array([0,137,77)  # filter for red ball
    hsvh = np.array([5,255,255])

while True: # starts loop to run camera

    # read current frame
    ret, frame = cap.read() # returns value of the feed, the image itself

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts feed to grayscale
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # converts feed to HSV

    # Display the resulting frame
    #cv2.imshow('frame1',frame) # displays raw feed
    #cv2.imshow('frame2',gray) # displays grayscale feed

    # get current positions of four trackbars
    hl = cv2.getTrackbarPos('hl','HSV') # name of trackbar, name of parent window (both ban be variables w/ strings)
    hh = cv2.getTrackbarPos('hh','HSV')
    sl = cv2.getTrackbarPos('sl','HSV')
    sh = cv2.getTrackbarPos('sh','HSV')
    vl = cv2.getTrackbarPos('vl','HSV')
    vh = cv2.getTrackbarPos('vh','HSV')
    #b=cv2.getTrackbarPos('blur','Blur')
    b=11
    hsvl = np.array([hl,sl,vl])
    hsvh = np.array([hh,sh,vh])

    #hsvl = np.array([0,130,102])  # resetting hsv thresholds for red ball
    #hsvh = np.array([28,255,255])

    mask = cv2.inRange(hsv, hsvl, hsvh) #inRange(image, lower_threshold_list, upper_threshold_list)
    #frame2 = cv2.bitwise_and(frame,frame,mask=mask) # magical function that applies your filter (mask) to an image
                                                    # (input image, output image, mask=whatever_your_mask_is)
    blur = cv2.GaussianBlur(mask,(b,b),0) # (image, blur size as a tuple, 0) blur size should be positive and odd
    #gray = cv2.cvtColor(blur,cv2.COLOR)

    frame2=cv2.bitwise_and(frame,frame,mask=blur)

    # adds text to window
    #cv2.putText(mask,'Lower HSV: [' + str(lh) +',' + str(ls) + ',' + str(lv) + ']', (10,30), font, 0.5, (200,255,155), 1, cv2.LINE_AA)
    #cv2.putText(mask,'Upper HSV: [' + str(uh) +',' + str(us) + ',' + str(uv) + ']', (10,60), font, 0.5, (200,255,155), 1, cv2.LINE_AA)

    cv2.imshow('Stock',hsv) # displays image stored in hsv
    cv2.imshow('HSV',frame2) # displays image stored in mask to window 'HSV'
    cv2.imshow('Blur',blur)
                           # (window name can be a variable storing a string)

    if cv2.waitKey(1) & 0xFF == ord('q'): # quits program if 'q' is pressed
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
