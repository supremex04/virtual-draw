import cv2 as cv
import keyboard
import numpy as np


frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4, frameHeight)
cap.set(10,100)      #10 is ID no. for brightness
# Set the desired FPS
desired_fps = 60  # Replace this with your desired FPS
cap.set(cv.CAP_PROP_FPS, desired_fps)

colors = [[49,120,62,179,255,255]]  
points = []

def colorDetect(img , color):
    HSVimg = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    newPoints = []
    for color in colors:
        lowerLimit = np.array(color[0:3])
        upperLimit = np.array(color[3:6])
        mask = cv.inRange(HSVimg, lowerLimit, upperLimit)
        x,y = contourDetect(mask)
        cv.circle(mirror, (x,y),7, (0,255,0), cv.FILLED)
        if (x !=0 and y !=0) and (keyboard.is_pressed("space")):
            newPoints.append([x,y])
        cv.imshow("Mask", mask)
        for point in newPoints:
            points.append(point)
        print(points)
        #print(newPoints)

def contourDetect(img):
    x,y,w,h = 0,0,0,0
    contours, hierarchy = cv.findContours(img , cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv.contourArea(contour)
        if area> 300:
            cv.drawContours(mirror,contour,-1,(0,255,0),3)
            perimeter = cv.arcLength(contour,True)
            approx = cv.approxPolyDP(contour,0.02*perimeter,True)
            x,y,w,h = cv.boundingRect(approx)
    return int(x+(w/2)) ,y

def draw(points):
        for point in points:
            cv.circle(mirror, (point[0], point[1]), 6, (0,255,0), cv.FILLED)


while True:
    feedback, img = cap.read()
    mirror = cv.flip(img,1)
    colorDetect(mirror, colors)
    if len(points) != 0:
        draw(points)

    cv.imshow("Capture", mirror)


    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break