import numpy as np
import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow('Stock')
cv2.namedWindow('HSV')

def nothing(x):
    print("Trackbar value: " + str(x))
    pass

uh = 0 #130
lh = 0 #110
us = 0 #255
ls = 0 #50
uv = 0 #255
lv = 0 #50

lower_hsv = np.array([lh,ls,lv])
upper_hsv = np.array([uh,us,uv])

# create trackbars for Upper HSV
cv2.createTrackbar('UpperH','HSV',0,255,nothing)
cv2.setTrackbarPos('UpperH','HSV', uh)

# create trackbars for Lower HSV
cv2.createTrackbar('LowerH','HSV',0,255,nothing)
cv2.setTrackbarPos('LowerH','HSV', lh)

cv2.createTrackbar('UpperS','HSV',0,255,nothing)
cv2.setTrackbarPos('UpperS','HSV', us)

cv2.createTrackbar('LowerS','HSV',0,255,nothing)
cv2.setTrackbarPos('LowerS','HSV', ls)

cv2.createTrackbar('UpperV','HSV',0,255,nothing)
cv2.setTrackbarPos('UpperV','HSV', uv)

cv2.createTrackbar('LowerV','HSV',0,255,nothing)
cv2.setTrackbarPos('LowerV','HSV', lv)

#font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret,frame=cap.read()

    # get current positions of trackbars
    uh = cv2.getTrackbarPos('UpperH','HSV')
    lh = cv2.getTrackbarPos('LowerH','HSV')
    us = cv2.getTrackbarPos('UpperS','HSV')
    ls = cv2.getTrackbarPos('LowerS','HSV')
    uv = cv2.getTrackbarPos('UpperV','HSV')
    lv = cv2.getTrackbarPos('LowerV','HSV')

    # store values in a list list to pass to threshold function (inRange function)
    upper_hsv = np.array([uh,us,uv])
    lower_hsv = np.array([lh,ls,lv])

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Creates threshold image based on HSV values from trackbars
    # (image matrix, HSV lower values stored as a list, HSV upper values stored as a list)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

    # adds text to window
    #cv2.putText(mask,'Lower HSV: [' + str(lh) +',' + str(ls) + ',' + str(lv) + ']', (10,30), font, 0.5, (200,255,155), 1, cv2.LINE_AA)
    #cv2.putText(mask,'Upper HSV: [' + str(uh) +',' + str(us) + ',' + str(uv) + ']', (10,60), font, 0.5, (200,255,155), 1, cv2.LINE_AA)

    # Displays image stored in mask
    cv2.imshow('HSV',mask)

    # kills program when 'esc' is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
