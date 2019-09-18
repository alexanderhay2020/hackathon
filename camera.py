# computer vision

import numpy as np
import cv2

def nothing(x):
    pass

cap=cv2.VideoCapture(2) # reads from 2nd camera (cv2.VideoCapture(0) is the webcam)
#img=cv2.imread('~/Pictures/Firefox_wallpaper.png',0) # reads image from a file

# creates windows named "HSV". Name can be an str variable
windowName0='camera'
windowName1='ConvexHull'
cv2.namedWindow(windowName0)
cv2.namedWindow(windowName1)

# creates 6 trackbars in window HSV, sets hi/low thresholds
cv2.createTrackbar('hl',windowName0,0,255,nothing) # (trackbar caption, parent window, preset val, max val,function called when trackbar moves)
cv2.createTrackbar('hh',windowName0,0,255,nothing)
cv2.createTrackbar('sl',windowName0,0,255,nothing)
cv2.createTrackbar('sh',windowName0,0,255,nothing)
cv2.createTrackbar('vl',windowName0,0,255,nothing)
cv2.createTrackbar('vh',windowName0,0,255,nothing)

def filter(img):

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # get current positions of four trackbars
    hl=cv2.getTrackbarPos('hl',windowName0) # name of trackbar, name of parent window (both ban be variables w/ strings)
    hh=cv2.getTrackbarPos('hh',windowName0)
    sl=cv2.getTrackbarPos('sl',windowName0)
    sh=cv2.getTrackbarPos('sh',windowName0)
    vl=cv2.getTrackbarPos('vl',windowName0)
    vh=cv2.getTrackbarPos('vh',windowName0)

    #hsvl=np.array([hl,sl,vl])
    hsvl=np.array([0,137,77])  # filter for red ball
    #hsvh=np.array([hh,sh,vh])
    hsvh=np.array([5,255,255])

    # applies threshold mask from hi/low HSV values
    mask=cv2.inRange(hsv, hsvl, hsvh)
    # applies Gaussian Blur
    blur=cv2.GaussianBlur(mask,(7,7),0)
    # applies mask to input img
    img=cv2.bitwise_and(img,img,mask=blur)
    # convert to grayscale
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    return img

def applyCircles(img):

    # finds circles in img
    #cv2.HoughCircles(img,circlescv2.HOUGH_GRADIENT,1,1,100,100,0,0)


    return

while True: # starts loop to run camera

    # read current frame
    ret,frame=cap.read() # returns value of the feed, the image itself

    frame=filter(frame)
    #frame=applyCircles(frame)

    detected_circles=cv2.HoughCircles(frame,cv2.HOUGH_GRADIENT, 1, 20, 50, 30, minRadius = 1, maxRadius = 255)

    if detected_circles is not None:
          # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            # Draw the circumference of the circle.
            cv2.circle(img, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
            cv2.imshow(windowName1, img)
            cv2.waitKey(0)

    contours,hierarchy=cv2.findContours(frame,1,2)
    cnt=max(contours)

    hull = cv2.convexHull(cnt)

    frame2 = cv2.drawContours(frame, contours, -1, (255,0,0), 3)

    cv2.imshow(windowName0,frame) # displays image stored in hsv
    cv2.imshow(windowName1,frame2)

    #drawing = np.zeros((frame.shape[0], frame.shape[1], 3), np.uint8)

    # draw contours and hull points

    if cv2.waitKey(1)&0xFF==ord('q'): # quits program if 'q' is pressed
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
