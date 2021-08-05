
from RobotMove import *
import time
from tryDect import Detect
m=0
robotSize = 2

def turnRight(robot):
    #turn right
    TURNR()
    print('turn right')
    if robot[2] == 3:
        robot[2] = 0
    else:
        robot[2] = robot[2] + 1
        
def turnLeft(robot):
    #turn left
    TURNL()
    print('turn left')
    if robot[2] == 0:
        robot[2] = 3
    else:
        robot[2] = robot[2] - 1
        
def turn180(robot):
    #turn 180
    for i in range(2):
     TURNR()
    print('Turn 180')
    if robot[2] == 2:
        robot[2] = 0
    elif robot[2] == 3:
        robot[2] = 1
    else:
        robot[2] = robot[2] + 2
        
def mov1(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y2 - y1 - 1
    for i in range(y2-y1-1):
     FORWARD()
    robot[1] = robot[1] + y2 - y1 - 1
    #turn right
    turnRight(robot)
    #go straight for x2 - x1 - 5
    for i in range(x2-x1-5):
     FORWARD()
    robot[0] = robot[0] +  x2 - x1 - 5
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov2(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 - 1
    for i in range (x2-x1-1):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 - 1
    #turn left
    turnLeft(robot)
    #go straight for y2 - y1 - 5
    for i in range (y2-y1-5):
     FORWARD()
    robot[1] = robot[1] +  y2 - y1 - 5
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov3(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 + 3
    for i in range (x2-x1+3):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 + 3
    #turn left
    turnLeft(robot)
    #go straight for y2 - y1 - 1
    for i in range (y2-y1-1):
     FORWARD()
    robot[1] = robot[1] +  y2 - y1 - 1
    #turn left
    turnLeft(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov4(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y2 - y1 + 3
    for i in range (y2-y1+3):
     FORWARD()
    robot[1] = robot[1] + y2 - y1 + 3
    #turn right
    turnRight(robot)
    #go straight for x2 - x1 - 1
    for i in range (x2-x1-1):
     FORWARD()
    robot[0] = robot[0] +  x2 - x1 - 1
    #turn right
    turnRight(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov5(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 5
    for i in range (x1 - x2 +5):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn right
    turnRight(robot)
    #go straight for y2 - y1 - 1
    for i in range (y2 -y1 -1):
     FORWARD()
    robot[1] = robot[1] +  y2 - y1 - 1
    #turn right
    turnRight(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov6(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 1
    for i in range (x1-x2+1):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn right
    turnRight(robot)
    #go straight for y2 - y1 - 5
    for i in range (y2-y1 -5):
     FORWARD()
    robot[1] = robot[1] +  y2 - y1 - 5
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov7(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y2 - y1 -1
    for i in range (y2-y1-1):
     FORWARD()
    robot[1] = robot[1] + y2 - y1 -1
    #turn left
    turnLeft(robot)
    #go straight for x1 - x2 - 3
    for i in range (x1 -x2 -3):
     FORWARD()
    robot[0] = robot[0] -  (x1 - x2 - 3)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov8(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y2 - y1 + 3
    for i in range (y2 - y1 +3):
     FORWARD()
    robot[1] = robot[1] + y2 - y1 + 3
    #turn left
    turnLeft(robot)
    #go straight for x1 - x2 + 1
    for i in range (x1-x2+1):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn left
    turnLeft(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov9(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 1
    for i in range (y1-y2+1):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 + 1)
    #turn left
    turnLeft(robot)
    #go straight for x2 - x1 - 5
    for i in range(x2-x1-5):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 - 5
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov10(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 5
    for i in range(y1-y2+5):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 + 5)
    #turn left
    turnLeft(robot)
    #go straight for x2 - x1 - 1
    for i in range (x2-x1-1):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 - 1
    #turn left
    turnLeft(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
        
def mov11(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 + 3
    for i in range (x2-x1+3):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 + 3
    #turn right
    turnRight(robot)
    #go straight for y1 - y2 + 1
    for i in range (y1-y2+1):
     FORWARD()
    robot[1] = robot[1] -  (y1 - y2 + 1)
    #turn right
    turnRight(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
        
def mov12(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 - 1
    for i in range (x2-x1-1):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 - 1
    #turn right
    turnRight(robot)
    #go straight for y1 - y2 - 3 
    for i in range (y1-y2-3):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 - 3) 
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov13(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 5
    for i in range (x1-x2+5):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn left
    turnLeft(robot)
    #go straight for y1 - y2 + 1
    for i in range (y1-y2+1):
     FORWARD()
    robot[1] = robot[1] -  (y1 - y2 + 1)
    #turn left
    turnLeft(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov14(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 5
    for i in range (y1-y2+5):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 + 5)
    #turn right
    turnRight(robot)
    #go straight for x1 - x2 + 1
    for i in range (x1-x2+1):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn right
    turnRight(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov15(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 1
    for i in range(y1-y2+1):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 + 1)
    #turn right
    turnRight(robot)
    #go straight for x1 - x2 - 3
    for i in range(x1-x2-3):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 - 3)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov16(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 1
    for i in range (x1-x2+1):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn left
    turnLeft(robot)
    #go straight for y1 - y2 - 3
    for i in range (y1-y2-3):
     FORWARD()
    robot[1] = robot[1] -  (y1 - y2 - 3)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov17(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 5
    for i in range (x1 - x2 + 5):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn right
    turnRight(robot)
    #go Straight for y2 - y1 - 1
    for i in range (y2 - y1 - 1):
     FORWARD()
    robot[1] = robot[1] + y2 - y1 - 1
    #turn right
    turnRight(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov18(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y2 - y1 - 5
    for i in range (y2 - y1 - 5):
     FORWARD()
    robot[1] = robot[1] + y2 - y1 - 5
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov19(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x2 - x1 + 3
    for i in range (x2 - x1 + 3):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 + 3
    #turn left
    turnLeft(robot)
    #go Straight for y2 - y1 - 1
    for i in range (y2 - y1 - 1):
     FORWARD()
    robot[1] = robot[1] + y2 - y1 - 1
    #turn left
    turnLeft(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov20(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x2 - x1 + 2
    for i in range (x2 - x1 + 2):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 + 2
    #turn left
    turnLeft(robot)
    #go Straight for y2 - y1 + 3
    for i in range (y2 - y1 + 3):
     FORWARD()
    robot[1] = robot[1] + y2 - y1 + 3 
    #turn left
    turnLeft(robot)
    #go Straight for 3
    for i in range (3):
     FORWARD()
    robot[0] = robot[0] - (3)
    #turn left
    turnLeft(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov21(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x1 - x2 + 5
    for i in range (x1 - x2 + 5):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn left
    turnLeft(robot)
    #go Straight for y1 - y2 + 1
    for i in range (y1 - y2 + 1):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 + 1)
    #turn left
    turnLeft(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov22(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x1 - x2 + 5
    for i in range (x1 - x2 + 5):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn left
    turnLeft(robot)
    #go Straight for y1 - y2 + 5
    for i in range (y1 - y2 + 5):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 + 5)
    #turn left
    turnLeft(robot)
    #go Straight for x1 - x2 + 5
    for i in range (x1 - x2 + 5):
     FORWARD()
    robot[0] = robot[0] + x1 - x2 + 5
    #turn left
    turnLeft(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov23(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x2 - x1 + 3
    for i in range (x2 - x1 + 3):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 + 3
    #turn right
    turnRight(robot)
    #go Straight for y1 - y2 + 1
    for i in range (y1 - y2 + 1):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 + 1)
    #turn right
    turnRight(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov24(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y1 - y2 - 3
    for i in range (y1 - y2 - 3):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 - 3)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov25(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x2 - x1 - 5
    for i in range (x2 - x1 - 5):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 - 5
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov26(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y1 - y2 + 5
    for i in range (y1 - y2 + 5):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 + 5)
    #turn left
    turnLeft(robot)
    #go Straight for x2 - x1 - 1
    for i in range (x2 - x1 - 1):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 - 1
    #turn left
    turnLeft(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov27(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y1 - y2 + 4
    for i in range (y1 - y2 + 4):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 + 4)
    #turn left
    turnLeft(robot)
    #go Straight for x2 - x1 + 3
    for i in range (x2 - x1 + 3):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 + 3
    #turn left
    turnLeft(robot)
    #go Straight for y1 - y2 + 4
    for i in range (y1 - y2 + 4):
     FORWARD()
    robot[1] = robot[1] + (y1 - y2 + 4)
    #turn left
    turnLeft(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov28(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y2 - y1 + 3
    for i in range (y2 - y1 + 3):
     FORWARD()
    robot[1] = robot[1] + y2 - y1 + 3
    #turn Right
    turnRight(robot)
    #go Straight for x2 - x1 - 1
    for i in range (x2 - x1 - 1):
     FORWARD()
    robot[0] = robot[0] + x2 - x1 - 1
    #turn Right
    turnRight(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)
    
def mov29(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y1 - y2 + 4
    for i in range (y1 - y2 + 4):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 + 4)
    #turn Right
    turnRight(robot)
    #go Straight for x1 - x2 + 5
    for i in range (x1 - x2 + 5):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn Right
    turnRight(robot)
    #go Straight for 30 cm
    for i in range (3):
     FORWARD()
    robot[1] = robot[1] + 3
    #turn Right
    turnRight(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov30(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y1 - y2 + 5
    for i in range (y1 - y2 + 5):
     FORWARD()
    robot[1] = robot[1] - (y1 - y2 + 5)
    #turn Right
    turnRight(robot)
    #go Straight for x1 - x2 + 1
    for i in range (x1 - x2 + 1):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn Right
    turnRight(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov31(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x1 - x2 - 3
    for i in range (x1 - x2 - 3):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 - 3)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)

def mov32(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y2 - y1 + 3
    for i in range (y2 - y1 + 3):
     FORWARD()
    robot[1] = robot[1] + (y2 - y1 + 3)
    #turn left
    turnLeft(robot)
    #go Straight for x1 - x2 + 1
    for i in range (x1 - x2 + 1):
     FORWARD()
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn left
    turnLeft(robot)
    detect=Detect()
    class_id = detect.main(m)
    obstacle_id = str((x2*100) +y2)
    return obstacle_id, int(class_id)    

def move(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    print('Origin',robot)
    if y2>y1 + robotSize: #top 
        if x2 > x1 + robotSize: #right 
            print('Des is top right of robot')
            if theta2 == 3:
                if theta1 == 0:
                    obid, imid = mov1(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov1(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov1(robot,end)
                    return obid, imid
                else:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov1(robot,end)
                    return obid, imid
            elif theta2 == 2:
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov2(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    obid, imid = mov2(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov2(robot,end)
                    return obid, imid
                else:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov2(robot,end)
                    return obid, imid
            elif theta2 == 1:
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov3(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    obid, imid = mov3(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov3(robot,end)
                    return obid, imid
                else:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov3(robot,end)
                    return obid, imid
            else:
                if theta1 == 0:
                    obid, imid = mov4(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov4(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov4(robot,end)
                    return obid, imid
                else:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov4(robot,end)
                    return obid, imid
        elif x2<x1: #left 
            print('Des is top left of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov5(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov5(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov5(robot,end)
                    return obid, imid
                else:
                    obid, imid = mov5(robot,end)
                    return obid, imid
            elif theta2 == 2: 
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov6(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov6(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov6(robot,end)
                    return obid, imid
                else:
                    obid, imid = mov6(robot,end)
                    return obid, imid
            elif theta2 == 1:
                if theta1 == 0:
                    obid, imid = mov7(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov7(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov7(robot,end)
                    return obid, imid
                else:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov7(robot,end)
                    return obid, imid
            else:
                if theta1 == 0:
                    obid, imid = mov8(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov8(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov8(robot,end)
                    return obid, imid
                else:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov8(robot,end)
                    return obid, imid
        else: 
            print('Des is top of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov17(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov17(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov17(robot,end)
                    return obid, imid
                else:
                    obid, imid = mov17(robot,end)
                    return obid, imid
            elif theta2 == 2:
                if theta1 == 0:
                    obid, imid = mov18(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov18(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov18(robot,end)
                    return obid, imid
                else:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov18(robot,end)
                    return obid, imid
            elif theta2 == 1:
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov19(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    obid, imid = mov19(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov19(robot,end)
                    return obid, imid
                else:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov19(robot,end)
                    return obid, imid
            else:
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov20(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    obid, imid = mov20(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov20(robot,end)
                    return obid, imid
                else:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov20(robot,end)
                    return obid, imid
            
    elif y2<y1: #bottom  
        if x2>x1 + robotSize: #right 
            print('Des is bottom right of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov9(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov9(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    obid, imid = mov9(robot,end)
                    return obid, imid
                else:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov9(robot,end)
                    return obid, imid
            elif theta2 == 2: 
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov10(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov10(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    obid, imid = mov10(robot,end)
                    return obid, imid
                else:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov10(robot,end)
                    return obid, imid
            elif theta2 == 1: 
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov11(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    obid, imid = mov11(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov11(robot,end)
                    return obid, imid
                else:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov11(robot,end)
                    return obid, imid
            else: 
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov12(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    obid, imid = mov12(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov12(robot,end)
                    return obid, imid
                else:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov12(robot,end)
                    return obid, imid
        elif x2<x1: #left 
            print('Des is bottom left of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov13(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov13(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov13(robot,end)
                    return obid, imid
                else:
                    obid, imid = mov13(robot,end)
                    return obid, imid
            elif theta2 == 2: 
                if theta1 == 0:
                     #turn 180
                    turn180(robot)
                    obid, imid = mov14(robot,end)
                    return obid, imid
                elif theta1 == 1:
                   #turn right
                    turnRight(robot)
                    obid, imid = mov14(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    obid, imid = mov14(robot,end)
                    return obid, imid
                else:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov14(robot,end)
                    return obid, imid
            elif theta2 == 1: 
                if theta1 == 0:
                     #turn 180
                    turn180(robot)
                    obid, imid = mov15(robot,end)
                    return obid, imid
                elif theta1 == 1:
                   #turn right
                    turnRight(robot)
                    obid, imid = mov15(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    obid, imid = mov15(robot,end)
                    return obid, imid
                else:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov15(robot,end)
                    return obid, imid
            else: 
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov16(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov16(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov16(robot,end)
                    return obid, imid
                else:
                    obid, imid = mov16(robot,end)
                    return obid, imid
        else: #bottom
            print('Des is bottom of the robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov21(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov21(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov21(robot,end)
                    return obid, imid
                else:
                    obid, imid = mov21(robot,end)
                    return obid, imid
            elif theta2 == 2: 
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov22(robot,end)
                    return obid, imid
                elif theta1 == 1:
                     #turn 180
                    turn180(robot)
                    obid, imid = mov22(robot,end)
                    return obid, imid
                elif theta1 == 2:
                   #turn right
                    turnRight(robot)
                    obid, imid = mov22(robot,end)
                    return obid, imid
                else:
                    obid, imid = mov22(robot,end)
                    return obid, imid
            elif theta2 == 1: 
                if theta1 == 0:
                    #turn right
                    turnRight(robot) 
                    obid, imid = mov23(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    obid, imid = mov23(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov23(robot,end)
                    return obid, imid
                else:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov23(robot,end)
                    return obid, imid
            else: 
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov24(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov24(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    obid, imid = mov24(robot,end)
                    return obid, imid
                else:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov24(robot,end)
                    return obid, imid
    
    else: #middle ###########################
        if x2 > x1 + robotSize: #right 
            print('Des is middle right of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov25(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    obid, imid = mov25(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov25(robot,end)
                    return obid, imid
                else:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov25(robot,end)
                    return obid, imid
            elif theta2 == 2:
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov26(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov26(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    obid, imid = mov26(robot,end)
                    return obid, imid
                else:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov26(robot,end)
                    return obid, imid
            elif theta2 == 1:
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov27(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov27(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    obid, imid = mov27(robot,end)
                    return obid, imid
                else:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov27(robot,end)
                    return obid, imid
            else:
                if theta1 == 0:
                    obid, imid = mov28(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov28(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov28(robot,end)
                    return obid, imid
                else:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov28(robot,end)
                    return obid, imid
        elif x2<x1: #left 
            print('Des is middle left of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov29(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov29(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    obid, imid = mov29(robot,end)
                    return obid, imid
                else:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov29(robot,end)
                    return obid, imid
            elif theta2 == 2: 
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov30(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov30(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    obid, imid = mov30(robot,end)
                    return obid, imid
                else:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov30(robot,end)
                    return obid, imid
            elif theta2 == 1:
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov31(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov31(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov31(robot,end)
                    return obid, imid
                else:
                    obid, imid = mov31(robot,end)
                    return obid, imid
            else:
                if theta1 == 0:
                    obid, imid = mov32(robot,end)
                    return obid, imid
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    obid, imid = mov32(robot,end)
                    return obid, imid
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    obid, imid = mov32(robot,end)
                    return obid, imid
                else:
                    #turn right
                    turnRight(robot)
                    obid, imid = mov32(robot,end)
                    return obid, imid
    print('end',robot)
