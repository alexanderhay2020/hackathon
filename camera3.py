import numpy as np
import cv2 as cv

cap=cv.VideoCapture(0)

while cap.isOpened():

    ret,img = cap.read()
    output = img.copy()

    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hsvl=np.array([0,161,77])  # filter for red ball
    hsvh=np.array([1,255,255])
    mask=cv.inRange(hsv, hsvl, hsvh)

    mask=cv.medianBlur(mask, 5)
    circles=cv.HoughCircles(mask, cv.HOUGH_GRADIENT, 1, 20,
                              param1=50, param2=30, minRadius=200, maxRadius=500)

    if circles is not None:
        detected_circles = np.uint16(np.around(circles))
        for (x, y ,r) in detected_circles[0, :]:
            cv.circle(output, (x, y), r, (0, 0, 0), 3)
            cv.circle(output, (x, y), 2, (0, 255, 255), 3)

    cv.imshow('mask',mask)
    cv.imshow('output',output)

    if cv.waitKey(1)&0xFF==ord('q'): # quits program if 'q' is pressed
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
