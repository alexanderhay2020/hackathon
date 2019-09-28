# computer vision

import numpy as np
import cv2

def nothing(x):
    pass

cap=cv2.VideoCapture(0) # reads from 2nd camera (cv2.VideoCapture(0) is the webcam)
#img=cv2.imread('~/Pictures/Firefox_wallpaper.png',0) # reads image from a file

# creates windows named "HSV". Name can be an str variable
windowName0='camera'
windowName1='contour'

cv2.namedWindow(windowName0)
cv2.namedWindow(windowName1)

# creates 6 trackbars in window HSV, sets hi/low thresholds
cv2.createTrackbar('hl',windowName0,0,255,nothing) # (trackbar caption, parent window, preset val, max val,function called when trackbar moves)
cv2.createTrackbar('hh',windowName0,0,255,nothing)
cv2.createTrackbar('sl',windowName0,0,255,nothing)
cv2.createTrackbar('sh',windowName0,0,255,nothing)
cv2.createTrackbar('vl',windowName0,0,255,nothing)
cv2.createTrackbar('vh',windowName0,0,255,nothing)

def filter(img): #filters image using various methods

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # get current positions of four trackbars
    hl=cv2.getTrackbarPos('hl',windowName0) # name of trackbar, name of parent window (both ban be variables w/ strings)
    hh=cv2.getTrackbarPos('hh',windowName0)
    sl=cv2.getTrackbarPos('sl',windowName0)
    sh=cv2.getTrackbarPos('sh',windowName0)
    vl=cv2.getTrackbarPos('vl',windowName0)
    vh=cv2.getTrackbarPos('vh',windowName0)

    #hsvl=np.array([hl,sl,vl])
    hsvl=np.array([0,161,77])  # filter for red ball
    #hsvh=np.array([hh,sh,vh])
    hsvh=np.array([1,255,255])

    # applies Gaussian Blur
    blur=cv2.GaussianBlur(hsv,(3,3),0)

    # applies threshold mask from hi/low HSV values
    mask=cv2.inRange(blur, hsvl, hsvh) # set to use blur

    # applies mask to input img (frame)
    # not need if all you want is a threshold image
    img=cv2.bitwise_and(frame,frame,mask=mask)

    # convert to grayscale
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    return mask

while cap.isOpened(): # starts loop to run camera

    # read current frame
    ret,frame=cap.read() # returns value of the feed, the image itself

    filtered_frame=filter(frame)
    #cv2.imshow(windowName0,filtered_frame)

    # this section finds and draws circles

    # circles = cv2.HoughCircles(filtered_frame, cv2.HOUGH_GRADIENT, 1, 20,
    #                           param1=50, param2=30, minRadius=0, maxRadius=0)
    # if circles is not None:
    #     detected_circles = np.uint16(np.around(circles))
    #     for (x, y ,r) in detected_circles[0, :]:
    #         cv.circle(output, (x, y), r, (0, 0, 0), 3)
    #         cv.circle(output, (x, y), 2, (0, 255, 255), 3)


    # this section finds and draws contours

    contours,hierarchy=cv2.findContours(filtered_frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    imgDrawn=cv2.drawContours(filtered_frame, contours, -1, (255,0,0), 5) # draws contours onto img
    cv2.imshow(windowName1,imgDrawn)
    print contours
    cv2.waitKey(0) # will wait for input to progress to next frame

    cv2.imshow(windowName0,frame)

    if cv2.waitKey(1)&0xFF==ord('q'): # quits program if 'q' is pressed
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
