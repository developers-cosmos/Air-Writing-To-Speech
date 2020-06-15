# import required packages
import cv2
import numpy as np
import time
s=int(input("enter 1.Blue color, 2.red color, 3.green color, 4.yellow color"))
a=[]
b=[]
while True:
    if s==1:
        a=[100, 60, 60]
        b=[140, 255, 255]
        #([110,50,50]) ([130,255,255])
        break
    elif s==2:
        a=[0,109,74]
        b=[180,255,255]
        break
    elif s==3:
        a=[0,70,107]
        b=[95,164,175]
        break
    elif s==4:
        a=[20,67,135]
        b=[27,255,255]
        break
    else:
        print("Invalid Input enter again")
colorIndex=1
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
#blue = True # enables to define blue color

#penval = []
#penval.append(np.array([88,109,76]))  # low hsv range for blue color
#penval.append(np.array([162,255,255])) # high hsv range for blue color

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

kernel = np.ones((5,5),np.uint8)

# Initializing the canvas on which we will draw
canvas = None

# Initilize x1,y1 points
x1,y1=0,0

# Threshold for noise
noiseth = 800
point = 0

while(1):
    _, frame = cap.read()
    frame = cv2.flip( frame, 1 )
    # Add the coloring options to the frame
    frame = cv2.rectangle(frame, (40,1), (160,65), (122,122,122), -1)
    frame = cv2.rectangle(frame, (210,1), (295,65), colors[0], -1)
    frame = cv2.rectangle(frame, (315,1), (410,65), colors[1], -1)
    frame = cv2.rectangle(frame, (445,1), (545,65), colors[2], -1)
    frame = cv2.rectangle(frame, (585,1), (680,65), colors[3], -1)
    cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (225, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (338, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (450, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (590, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)
    
    # Initialize the canvas as a black image of the same size as the frame.
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
    lower_range  = np.array(a)
    upper_range = np.array(b)
    
    mask = cv2.inRange(hsv, lower_range, upper_range)
    
    # Perform morphological operations to get rid of the noise
    mask = cv2.erode(mask,kernel,iterations = 1)
    mask = cv2.dilate(mask,kernel,iterations = 2)
    
    # Find Contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Make sure there is a contour present and also its size is bigger than 
    # the noise threshold.
    if contours and cv2.contourArea(max(contours, 
                                 key = cv2.contourArea)) > noiseth:
                
        c = max(contours, key = cv2.contourArea)    
        x2,y2,w,h = cv2.boundingRect(c)
        if y2 <= 65:
            if 40 <= x2 <= 150: # Clear All
                canvas =np.zeros_like(frame)
            elif 200 <= x2 <= 285:
                    colorIndex = 0 # Blue
            elif 315 <= x2 <= 410:
                    colorIndex = 1 # Green
            elif 445 <= x2 <= 545:
                    colorIndex = 2 # Red
            elif 585 <= x2 <= 680:
                    colorIndex = 3 # Yellow

        
        # If there were no previous points then save the detected x2,y2 as coordinates as x1,y1. 
        if x1 == 0 and y1 == 0:
            x1,y1= x2,y2    
        else:
            # Draw the line on the canvas
            canvas = cv2.line(canvas, (x1,y1),(x2,y2), colors[colorIndex], 8)
        
        # After the line is drawn the new points become the previous points.
        x1,y1= x2,y2

    else:
        # If there were no contours detected then make x1,y1 = 0
        x1,y1 =x2,y2
    
    # Merge the canvas and the frame.
    frame = cv2.add(frame,canvas)
    
    
    # Optionally stack both frames and show it.
    stacked = np.hstack((canvas,frame))
    cv2.imshow('Track me if you can',cv2.resize(stacked,None,fx=0.6,fy=0.6))

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
        
    # When c is pressed store the current frame
    if k == ord('c'):
        cv2.imwrite('images/result'+str(point)+'.jpg',canvas)
        canvas = None
    point += 1

cv2.destroyAllWindows()
cap.release()
