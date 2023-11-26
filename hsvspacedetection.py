#trackbars for HSV space detection

#101 113 153 255 50 255
import cv2 as cv
import numpy as np

def empty(a):
    pass

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars", 620, 300)

cv.createTrackbar("Hue Min", "TrackBars", 49,179, empty)   
cv.createTrackbar("Sat Min", "TrackBars", 120,255, empty)
cv.createTrackbar("Value Min", "TrackBars", 62,255, empty)
cv.createTrackbar("Hue Max", "TrackBars", 179,179, empty)
cv.createTrackbar("Sat Max", "TrackBars", 222,255, empty)
cv.createTrackbar("Value Max", "TrackBars", 255,255, empty)

while True:
    
    success, img = cap.read()
    HSVimg = cv.cvtColor(img, cv.COLOR_BGR2HSV)


    h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    v_min = cv.getTrackbarPos("Value Min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_max = cv.getTrackbarPos("Value Max", "TrackBars")

    lowerLimit = np.array([h_min, s_min, v_min])
    upperLimit = np.array([h_max, s_max, v_max])
    mask = cv.inRange(HSVimg, lowerLimit, upperLimit)
    
    cv.imshow("Video",img)
    cv.imshow("HSV Video", HSVimg)
    cv.imshow("Mask", mask)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break