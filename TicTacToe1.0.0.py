import cv2
from time import sleep
import numpy as np
import cv2 as cv
import argparse
import random
import serial


ser=serial.Serial("/dev/ttyACM0",9600)
vc = cv2.VideoCapture(0)
cv2.namedWindow("Let's Play!")
A=[[0,0,0],
    [0,0,0],
    [0,0,0]]
i=0
val=0
delayTime = .1

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False



while rval == True:
    cv2.imshow("Let's Play!", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
   
    
    if key == 27: # exit on ESC
        break
    if key == 32:
        i=0
        # SPACE pressed
        img_name = "opencv_frame_0.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        
        sleep(delayTime)
        img = cv.imread('opencv_frame_0.png',0)
        img = cv.medianBlur(img,5)
        cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
        output = img.copy()
        circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                                    param1=100,param2=50,minRadius=0,maxRadius=0)
        circles = np.uint16(np.around(circles))
        if len(circles) > 0:
            circles = np.round(circles[0, :]).astype("int")
            print('the circles are', circles)
            
            for (x,y,r) in circles:
                cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(output,(x-5, y-5),(x+5, y+5),(0, 128, 255),-1)
                
            
            for k in circles:
                if circles[i][0]>0 and circles[i][0]<210 and circles[i][1]>0 and circles[i][1]<160:
                    print("Circle in square 1")
                    sleep(delayTime)
                    A[0][0]=1
                    i=i+1
                elif circles[i][0]>210 and circles[i][0]<420 and circles[i][1]>0 and circles[i][1]<160:
                    print("Circle in square 2")
                    sleep(delayTime)
                    A[0][1]=1
                    i=i+1
                elif circles[i][0]>420 and circles[i][1]>0 and circles[i][1]<160:
                    print("Circle in square 3")
                    sleep(delayTime)
                    A[0][2]=1
                    i=i+1
                elif circles[i][0]>0 and circles[i][0]<210 and circles[i][1]>160 and circles[i][1]<320:
                    print("Circle in square 4")
                    sleep(delayTime)
                    A[1][0]=1
                    i=i+1
                elif circles[i][0]>210 and circles[i][0]<420 and circles[i][1]>160 and circles[i][1]<320:
                    print("Circle in square 5")
                    sleep(delayTime)
                    A[1][1]=1
                    i=i+1
                elif circles[i][0]>420 and circles[i][1]>160 and circles[i][1]<320:
                    print("Circle in square 6")
                    sleep(delayTime)
                    A[1][2]=1
                    i=i+1
                elif circles[i][0]>0 and circles[i][0]<210 and circles[i][1]>320:
                    print("Circle in square 7")
                    sleep(delayTime)
                    A[2][0]=1
                    i=i+1
                elif circles[i][0]>210 and circles[i][0]<420 and circles[i][1]>320:
                    print("Circle in square 8")
                    sleep(delayTime)
                    A[2][1]=1
                    i=i+1
                elif circles[i][0]>420 and circles[i][1]>320:
                    print("Circle in square 9")
                    sleep(delayTime)
                    A[2][2]=1
                    i=i+1
                else:
                    print("circle not on board")
                    sleep(delayTime)
                    i=i+1
             
            
            if A[0][0]==A[0][1]==A[0][2]==1:
                print("Person Victory")
                break
            elif A[1][0]==A[1][1]==A[1][2]==1:
                print("Person Victory")
                break
            elif A[2][0]==A[2][1]==A[2][2]==1:
                print("Person Victory")
                break
            elif A[0][0]==A[1][0]==A[2][0]==1:
                print("Person Victory")
                break
            elif A[0][1]==A[1][1]==A[2][1]==1:
                print("Person Victory")
                break           
            elif A[0][2]==A[1][2]==A[2][2]==1:
                print("Person Victory")
                break           
            elif A[0][0]==A[1][1]==A[2][2]==1:
                print("Person Victory")
                break           
            elif A[0][2]==A[1][1]==A[2][0]==1:
                print("Person Victory")
                break
            elif 0 not in A[0] and 0 not in A[1] and 0 not in A[2]:
                print('Cats Game')
                break
                
            print("Before:",A)
          
            width = len(A[0])
            posn = 0
            found = []
            for row in A:
                for col in row:
                        if col == val:
                            found.append((posn // width, posn % width))
                        posn += 1

            
            move = random.choice(found)
            A[move[0]][move[1]]=2
            Random_move=[move[0],move[1]]
            print("found",found)
            if Random_move == [0,0]:
                Robot_Play = '1'
                ser.write(str.encode(Robot_Play))
                print("Robot plays in square ",Robot_Play)
                ser.flushInput()
            elif Random_move == [0,1]:
                Robot_Play = '2'
                ser.write(str.encode(Robot_Play))
                print("Robot plays in square ",Robot_Play)
                ser.flushInput()
            elif Random_move == [0,2]:
                Robot_Play = '3'
                ser.write(str.encode(Robot_Play))
                print("Robot plays in square ",Robot_Play)
                ser.flushInput()
            elif Random_move == [1,0]:
                Robot_Play = '4'
                ser.write(str.encode(Robot_Play))
                print("Robot plays in square ",Robot_Play)
                ser.flushInput()
            elif Random_move == [1,1]:
                Robot_Play = '5'
                ser.write(str.encode(Robot_Play))
                print("Robot plays in square ",Robot_Play)
                ser.flushInput()
            elif Random_move == [1,2]:
                Robot_Play = '6'
                ser.write(str.encode(Robot_Play))
                print("Robot plays in square ",Robot_Play)
                ser.flushInput()
            elif Random_move == [2,0]:
                Robot_Play = '7'
                ser.write(str.encode(Robot_Play))
                print("Robot plays in square ",Robot_Play)
                ser.flushInput()
            elif Random_move == [2,1]:
                Robot_Play = '8'
                ser.write(str.encode(Robot_Play))
                print("Robot plays in square ",Robot_Play)
                ser.flushInput()
            elif Random_move == [2,2]:
                Robot_Play = '9'
                ser.write(str.encode(Robot_Play))
                print("Robot plays in square ",Robot_Play)
                ser.flushInput()
            
            
                
                
                
            #cv2.line(img=frame, pt1=((move[0]*210)+105,((move[1]*160)+80)), pt2=((move[0]*210)+115,((move[1]*160)+90)), color=(125, 125, 0), thickness=10, lineType=8, shift=0)
            #cv2.circle(frame, ((move[0]*210)+105, (move[1]*160)+80), 5, (100, 100, 0), -1)
            #cv2.imwrite(img_name, frame)
            '''make robot place at A[move[0]][move[1]]'''
            print("After:",A)
            print("---------------------------")

            if A[0][0]==A[0][1]==A[0][2]==2:
                print("Robot Victory")
                break
            elif A[1][0]==A[1][1]==A[1][2]==2:
                print("Robot Victory")
                break
            elif A[2][0]==A[2][1]==A[2][2]==2:
                print("Robot Victory")
                break
            elif A[0][0]==A[1][0]==A[2][0]==2:
                print("Robot Victory")
                break
            elif A[0][1]==A[1][1]==A[2][1]==2:
                print("Robot Victory")
                break           
            elif A[0][2]==A[1][2]==A[2][2]==2:
                print("Robot Victory")
                break           
            elif A[0][0]==A[1][1]==A[2][2]==2:
                print("Robot Victory")
                break           
            elif A[0][2]==A[1][1]==A[2][0]==2:
                print("Robot Victory")
                break
            elif 0 not in A[0] and 0 not in A[1] and 0 not in A[2]:
                print('Cats Game')
                break
                      
                    
                      

        else:
            print("TRY AGAIN")
        
                
            
            
            
        

        #cv.imshow('detected circles',np.hstack([output]))
        
                   
    else:
        cv2.line(img=frame, pt1=(0, 160), pt2=(800, 160), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
        cv2.line(img=frame, pt1=(0, 320), pt2=(800, 320), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
        cv2.line(img=frame, pt1=(210, 0), pt2=(210, 800), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
        cv2.line(img=frame, pt1=(420, 0), pt2=(420, 800), color=(255, 0, 0), thickness=5, lineType=8, shift=0)

   


vc.release()
cv2.destroyWindow("Let's Play!") 


