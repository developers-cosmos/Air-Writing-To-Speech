#imports
from tkinter import *
import cv2
import numpy as np
import time
from datetime import datetime
from playsound import playsound

def drawing(s):
    
    if s==1:
        a=[100, 60, 60]
        b=[140, 255, 255]
        print("blue")
        #([110,50,50]) ([130,255,255])
    elif s==2:
        a=[0,109,74]
        b=[180,255,255]
        print("red")
        
    elif s==3:
        a=[0,70,107]
        b=[95,164,175]
        print("green")
    elif s==4:
        a=[20,67,135]
        b=[27,255,255]
        print("yellow")

    colorIndex=s-1
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255),(0,0,0)]


    cap = cv2.VideoCapture(0)
    cap.set(3,1280)
    cap.set(4,720)

    kernel = np.ones((5,5),np.uint8)

    # Initializing the canvas on which we will draw
    canvas = None

    # Initilize x1,y1,x2,y2 points
    x1, y1 = 0, 0
    x2, y2 = 0, 0

    # Threshold for noise
    noiseth = 800

    while(1):
        
        _, frame = cap.read()
        frame = cv2.flip( frame, 1 )
        # Add the coloring options to the frame
        frame = cv2.rectangle(frame, (40,1), (180,55), (0,0,0), -1)
        frame = cv2.rectangle(frame, (220,1), (360,55),(0,0,0) , -1)
        frame = cv2.rectangle(frame, (400,1), (540,55), (0,0,0), -1)
        frame = cv2.rectangle(frame, (580,1), (720,55), (0,0,0), -1)
        frame = cv2.rectangle(frame, (760,1), (900,55),(0,0,0), -1)
        frame = cv2.rectangle(frame, (940,1), (1080,55), (0,0,0), -1)
        frame = cv2.rectangle(frame, (1120,1), (1260,55), (0,0,0), -1)
        cv2.putText(frame, "YELLOW", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "BLUE", (240, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "GREEN", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "RED", (600, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "ERASER", (780, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)
        cv2.putText(frame, "CLEAR", (960, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)
        cv2.putText(frame, "CAPTURE", (1140, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA) 
        # Initialize the canvas as a black image of the same size as the frame.
        if canvas is None:
            canvas = np.zeros_like(frame)

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
        lower_range  = np.array(a)
        upper_range = np.array(b)
    
        mask = cv2.inRange(hsv, lower_range, upper_range)
    
        #    Perform morphological operations to get rid of the noise
        mask = cv2.erode(mask,kernel,iterations = 1)
        mask = cv2.dilate(mask,kernel,iterations = 2)
    
        # Find Contours
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        # Make sure there is a contour present and also its size is bigger than 
        # the noise threshold.
        if contours and cv2.contourArea(max(contours,key = cv2.contourArea)) > noiseth:
                
            c = max(contours, key = cv2.contourArea)    
            x2,y2,w,h = cv2.boundingRect(c)
            if y2 <= 65:
                if 40 <= x2 <= 180: # yellow
                    colorIndex=3
                elif 220 <= x2 <= 360:
                    colorIndex = 0 # Blue
                elif 400 <= x2 <= 540:
                    colorIndex = 1 # Green
                elif 580 <= x2 <= 720:
                    colorIndex = 2 # Red
                elif 760 <= x2 <= 900: #eraser
                    colorIndex=4
                elif 940 <=x2<= 1080: #clear
                    canvas =np.zeros_like(frame)
                    
                elif 1120 <= x2 <=1260: #capture
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    playsound('camera.mp3')
                    f='images/'+current_time[0:2]+current_time[3:5]+current_time[6:]+'.jpg'
                    cv2.imwrite(f,canvas)
                   
                                                            
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
            x1,y1 =0,0
    
        # Merge the canvas and the frame.
        frame = cv2.add(frame,canvas)
    
    
        # Optionally stack both frames and show it.
        stacked = np.hstack((canvas,frame))
        cv2.imshow('Track Me If You Can',cv2.resize(stacked,None,fx=0.6,fy=1.01))

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
        # When c is pressed store the current frame
        if k == ord('c'):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            playsound('camera.mp3')
            f='images/'+current_time[0:2]+current_time[3:5]+current_time[6:]+'.jpg'
            print(f)
            cv2.imwrite(f,canvas)
            canvas = None

    cv2.destroyAllWindows()
    cap.release()
    
def drawing1():
    drawing(1)
def drawing2():
    drawing(2)
def drawing3():
    drawing(3)
def drawing4():
    drawing(4)
window = Tk()
window.title("Welcome to DC")
window.geometry('1928x1080')
lbl = Label(window, text="SELECT ANY BUTTON TO PICK COLOR",font=("Times New Roman",20,"bold"),pady=8, bd=6,justify=LEFT).pack()
# create button
lbl=Label(window,pady=80).pack()
button1 = Button(window, text='BLUE COLOR',font=("Times New Roman",15,"bold"), width=40, height=3, bg='#0052cc', fg='#000000', activebackground='#0052cc', activeforeground='#aaffaa',command=drawing1)
# add button to gui window
button1.pack()
lbl=Label(window,pady=10).pack()
button2 = Button(window, text='RED COLOR',font=("Times New Roman",15,"bold"), width=40, height=3, bg='#ff0000', fg='#000000', activebackground='#ff0000', activeforeground='#aaffaa',command=drawing2)
# add button to gui window
button2.pack()
lbl=Label(window,pady=10).pack()
button3 = Button(window, text='GREEN COLOR',font=("Times New Roman",15,"bold"), width=40, height=3, bg='#00ff00', fg='#000000', activebackground='#00ff00', activeforeground='#aaffaa',command=drawing3)
# add button to gui window
button3.pack()
lbl=Label(window,pady=10).pack()
button4 = Button(window, text='YELLOW COLOR',font=("Times New Roman",15,"bold"), width=40, height=3, bg='#ffff00', fg='#000000', activebackground='#ffff00', activeforeground='#aaffaa',command=drawing4)
# add button to gui window
button4.pack()
window.mainloop()
