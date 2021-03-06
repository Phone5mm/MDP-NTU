
robotSize = 2

def turnRight(robot):
    #turn right
    if robot[2] == 3:
        robot[2] = 0
    else:
        robot[2] = robot[2] + 1
        
def turnLeft(robot):
    #turn left
    if robot[2] == 0:
        robot[2] = 3
    else:
        robot[2] = robot[2] - 1
        
def turn180(robot):
    #turn 180
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
        robot[1] = robot[1] + 1
    #turn right
    turnRight(robot)
    #go straight for x2 - x1 - 5
    for i in range(x2 - x1 - 5):
        robot[0] = robot[0] + 1

def mov2(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 - 1
    robot[0] = robot[0] + x2 - x1 - 1
    #turn left
    turnLeft(robot)
    #go straight for y2 - y1 - 5
    robot[1] = robot[1] +  y2 - y1 - 5

def mov3(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 + 3
    robot[0] = robot[0] + x2 - x1 + 3
    #turn left
    turnLeft(robot)
    #go straight for y2 - y1 - 1
    robot[1] = robot[1] +  y2 - y1 - 1
    #turn left
    turnLeft(robot)

def mov4(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y2 - y1 + 3
    robot[1] = robot[1] + y2 - y1 + 3
    #turn right
    turnRight(robot)
    #go straight for x2 - x1 - 1
    robot[0] = robot[0] +  x2 - x1 - 1
    #turn right
    turnRight(robot)
    
def mov5(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 5
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn right
    turnRight(robot)
    #go straight for y2 - y1 - 1
    robot[1] = robot[1] +  y2 - y1 - 1
    #turn right
    turnRight(robot)

def mov6(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 1
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn right
    turnRight(robot)
    #go straight for y2 - y1 - 5
    robot[1] = robot[1] +  y2 - y1 - 5

def mov7(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y2 - y1 -1
    robot[1] = robot[1] + y2 - y1 -1
    #turn left
    turnLeft(robot)
    #go straight for x1 - x2 - 3
    robot[0] = robot[0] -  (x1 - x2 - 3)

def mov8(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y2 - y1 + 3
    robot[1] = robot[1] + y2 - y1 + 3
    #turn left
    turnLeft(robot)
    #go straight for x1 - x2 + 1
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn left
    turnLeft(robot)

def mov9(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 1
    robot[1] = robot[1] - (y1 - y2 + 1)
    #turn left
    turnLeft(robot)
    #go straight for x2 - x1 - 5
    robot[0] = robot[0] + x2 - x1 - 5

def mov10(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 5
    robot[1] = robot[1] - (y1 - y2 + 5)
    #turn left
    turnLeft(robot)
    #go straight for x2 - x1 - 1
    robot[0] = robot[0] + x2 - x1 - 1
    #turn left
    turnLeft(robot)
    
def mov11(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 + 3
    robot[0] = robot[0] + x2 - x1 + 3
    #turn right
    turnRight(robot)
    #go straight for y1 - y2 + 1
    robot[1] = robot[1] -  (y1 - y2 + 1)
    #turn right
    turnRight(robot)
    
def mov12(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x2 - x1 - 1
    robot[0] = robot[0] + x2 - x1 - 1
    #turn right
    turnRight(robot)
    #go straight for y1 - y2 - 3 
    robot[1] = robot[1] - (y1 - y2 - 3) 

def mov13(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 5
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn left
    turnLeft(robot)
    #go straight for y1 - y2 + 1
    robot[1] = robot[1] -  (y1 - y2 + 1)
    #turn left
    turnLeft(robot)

def mov14(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 5
    robot[1] = robot[1] - (y1 - y2 + 5)
    #turn right
    turnRight(robot)
    #go straight for x1 - x2 + 1
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn right
    turnRight(robot)

def mov15(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for y1 - y2 + 1
    robot[1] = robot[1] - (y1 - y2 + 1)
    #turn right
    turnRight(robot)
    #go straight for x1 - x2 - 3
    robot[0] = robot[0] - (x1 - x2 - 3)

def mov16(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 1
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn left
    turnLeft(robot)
    #go straight for y1 - y2 - 3
    robot[1] = robot[1] -  (y1 - y2 - 3)

def mov17(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go straight for x1 - x2 + 5
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn right
    turnRight(robot)
    #go Straight for y2 - y1 - 1
    robot[1] = robot[1] + y2 - y1 - 1
    #turn right
    turnRight(robot)

def mov18(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y2 - y1 - 5
    robot[1] = robot[1] + y2 - y1 - 5

def mov19(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x2 - x1 + 3
    robot[0] = robot[0] + x2 - x1 + 3
    #turn left
    turnLeft(robot)
    #go Straight for y2 - y1 - 1
    robot[1] = robot[1] + y2 - y1 - 1
    #turn left
    turnLeft(robot)

def mov20(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x2 - x1 + 2
    robot[0] = robot[0] + x2 - x1 + 2
    #turn left
    turnLeft(robot)
    #go Straight for y2 - y1 + 3
    robot[1] = robot[1] + y2 - y1 + 3 
    #turn left
    turnLeft(robot)
    #go Straight for x2 - x1 + 2
    robot[0] = robot[0] - (x2 - x1 + 2)
    #turn left
    turnLeft(robot)

def mov21(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x1 - x2 + 5
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn left
    turnLeft(robot)
    #go Straight for y1 - y2 + 1
    robot[1] = robot[1] - (y1 - y2 + 1)
    #turn left
    turnLeft(robot)

def mov22(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x1 - x2 + 5
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn left
    turnLeft(robot)
    #go Straight for y1 - y2 + 5
    robot[1] = robot[1] - (y1 - y2 + 5)
    #turn left
    turnLeft(robot)
    #go Straight for x1 - x2 + 5
    robot[0] = robot[0] + x1 - x2 + 5
    #turn left
    turnLeft(robot)

def mov23(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x2 - x1 + 3
    robot[0] = robot[0] + x2 - x1 + 3
    #turn right
    turnRight(robot)
    #go Straight for y1 - y2 + 1
    robot[1] = robot[1] - (y1 - y2 + 1)
    #turn right
    turnRight(robot)

def mov24(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y1 - y2 - 3
    robot[1] = robot[1] - (y1 - y2 - 3)

def mov25(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x2 - x1 - 5
    robot[0] = robot[0] + x2 - x1 - 5
    
def mov26(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y1 - y2 + 5
    robot[1] = robot[1] - (y1 - y2 + 5)
    #turn left
    turnLeft(robot)
    #go Straight for x2 - x1 - 1
    robot[0] = robot[0] + x2 - x1 - 1
    #turn left
    turnLeft(robot)
    
def mov27(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y1 - y2 + 4
    robot[1] = robot[1] - (y1 - y2 + 4)
    #turn left
    turnLeft(robot)
    #go Straight for x2 - x1 + 3
    robot[0] = robot[0] + x2 - x1 + 3
    #turn left
    turnLeft(robot)
    #go Straight for y1 - y2 + 4
    robot[1] = robot[1] + (y1 - y2 + 4)
    
def mov28(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y2 - y1 + 3
    robot[1] = robot[1] + y2 - y1 + 3
    #turn Right
    turnRight(robot)
    #go Straight for x2 - x1 - 1
    robot[0] = robot[0] + x2 - x1 - 1
    #turn Right
    turnRight(robot)
    
def mov29(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y1 - y2 + 4
    robot[1] = robot[1] - (y1 - y2 + 4)
    #turn Right
    turnRight(robot)
    #go Straight for x1 - x2 + 5
    robot[0] = robot[0] - (x1 - x2 + 5)
    #turn Right
    turnRight(robot)
    #go Straight for 30 cm
    robot[1] = robot[1] + 3
    #turn Right
    turnRight(robot)

def mov30(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y1 - y2 + 5
    robot[1] = robot[1] - (y1 - y2 + 5)
    #turn Right
    turnRight(robot)
    #go Straight for x1 - x2 + 1
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn Right
    turnRight(robot)
    
def mov31(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for x1 - x2 - 3
    robot[0] = robot[0] - (x1 - x2 - 3)

def mov32(robot,end):
    x1 = robot[0]
    x2 = end[0]
    y1 = robot[1]
    y2 = end[1]
    theta1 = robot[2]
    theta2 = end[2]
    #go Straight for y2 - y1 + 3
    robot[1] = robot[1] + (y2 - y1 + 3)
    #turn left
    turnLeft(robot)
    #go Straight for x1 - x2 + 1
    robot[0] = robot[0] - (x1 - x2 + 1)
    #turn left
    turnLeft(robot)
        
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
                    mov1(robot,end)
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    mov1(robot,end)
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    mov1(robot,end)
                else:
                    #turn right
                    turnRight(robot)
                    mov1(robot,end)
            elif theta2 == 2:
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    mov2(robot,end)
                elif theta1 == 1:
                    mov2(robot,end)
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    mov2(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov2(robot,end)
            elif theta2 == 1:
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    mov3(robot,end)
                elif theta1 == 1:
                    mov3(robot,end)
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    mov3(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov3(robot,end)
            else:
                if theta1 == 0:
                    mov4(robot,end)
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    mov4(robot,end)
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    mov4(robot,end)
                else:
                    #turn right
                    turnRight(robot)
                    mov4(robot,end)
        elif x2<x1: #left 
            print('Des is top left of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov5(robot,end)
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    mov5(robot,end)
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    mov5(robot,end)
                else:
                    mov5(robot,end)
            elif theta2 == 2: 
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov6(robot,end)
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    mov6(robot,end)
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    mov6(robot,end)
                else:
                    mov6(robot,end)
            elif theta2 == 1:
                if theta1 == 0:
                    mov7(robot,end)
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    mov7(robot,end)
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    mov7(robot,end)
                else:
                    #turn right
                    turnRight(robot)
                    mov7(robot,end)
            else:
                if theta1 == 0:
                    mov8(robot,end)
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    mov8(robot,end)
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    mov8(robot,end)
                else:
                    #turn right
                    turnRight(robot)
                    mov8(robot,end)
        else: 
            print('Des is top of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov17(robot,end)
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    mov17(robot,end)
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    mov17(robot,end)
                else:
                    mov17(robot,end)
            elif theta2 == 2:
                if theta1 == 0:
                    mov18(robot,end)
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    mov18(robot,end)
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    mov18(robot,end)
                else:
                    #turn right
                    turnRight(robot)
                    mov18(robot,end)
            elif theta2 == 1:
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    mov19(robot,end)
                elif theta1 == 1:
                    mov19(robot,end)
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    mov19(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov19(robot,end)
            else:
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    mov20(robot,end)
                elif theta1 == 1:
                    mov20(robot,end)
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    mov20(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov20(robot,end)
            
    elif y2<y1: #bottom  
        if x2>x1 + robotSize: #right 
            print('Des is bottom right of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    mov9(robot,end)
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    mov9(robot,end)
                elif theta1 == 2:
                    mov9(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov9(robot,end)
            elif theta2 == 2: 
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    mov10(robot,end)
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    mov10(robot,end)
                elif theta1 == 2:
                    mov10(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov10(robot,end)
            elif theta2 == 1: 
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    mov11(robot,end)
                elif theta1 == 1:
                    mov11(robot,end)
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    mov11(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov11(robot,end)
            else: 
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    mov12(robot,end)
                elif theta1 == 1:
                    mov12(robot,end)
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    mov12(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov12(robot,end)
        elif x2<x1: #left 
            print('Des is bottom left of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov13(robot,end)
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    mov13(robot,end)
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    mov13(robot,end)
                else:
                    mov13(robot,end)
            elif theta2 == 2: 
                if theta1 == 0:
                     #turn 180
                    turn180(robot)
                    mov14(robot,end)
                elif theta1 == 1:
                   #turn right
                    turnRight(robot)
                    mov14(robot,end)
                elif theta1 == 2:
                    mov14(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov14(robot,end)
            elif theta2 == 1: 
                if theta1 == 0:
                     #turn 180
                    turn180(robot)
                    mov15(robot,end)
                elif theta1 == 1:
                   #turn right
                    turnRight(robot)
                    mov15(robot,end)
                elif theta1 == 2:
                    mov15(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov15(robot,end)
            else: 
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov16(robot,end)
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    mov16(robot,end)
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    mov16(robot,end)
                else:
                    mov16(robot,end)
        else: #bottom
            print('Des is bottom of the robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov21(robot,end)
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    mov21(robot,end)
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    mov21(robot,end)
                else:
                    mov21(robot,end)
            elif theta2 == 2: 
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov22(robot,end)
                elif theta1 == 1:
                     #turn 180
                    turn180(robot)
                    mov22(robot,end)
                elif theta1 == 2:
                   #turn right
                    turnRight(robot)
                    mov22(robot,end)
                else:
                    mov22(robot,end)
            elif theta2 == 1: 
                if theta1 == 0:
                    #turn right
                    turnRight(robot) 
                    mov23(robot,end)
                elif theta1 == 1:
                    mov23(robot,end)
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    mov23(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov23(robot,end)
            else: 
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    mov24(robot,end)
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    mov24(robot,end)
                elif theta1 == 2:
                    mov24(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov24(robot,end)
    
    else: #middle ###########################
        if x2 > x1 + robotSize: #right 
            print('Des is middle right of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn right
                    turnRight(robot)
                    mov25(robot,end)
                elif theta1 == 1:
                    mov25(robot,end)
                elif theta1 == 2:
                    #turn left
                    turnLeft(robot)
                    mov25(robot,end)
                else:
                    #turn 180
                    turn180(robot)
                    mov25(robot,end)
            elif theta2 == 2:
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    mov26(robot,end)
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    mov26(robot,end)
                elif theta1 == 2:
                    mov26(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov26(robot,end)
            elif theta2 == 1:
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    mov27(robot,end)
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    mov27(robot,end)
                elif theta1 == 2:
                    mov27(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov27(robot,end)
            else:
                if theta1 == 0:
                    mov28(robot,end)
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    mov28(robot,end)
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    mov28(robot,end)
                else:
                    #turn right
                    turnRight(robot)
                    mov28(robot,end)
        elif x2<x1: #left 
            print('Des is middle left of robot')
            if theta2 == 3:
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    mov29(robot,end)
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    mov29(robot,end)
                elif theta1 == 2:
                    mov29(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov29(robot,end)
            elif theta2 == 2: 
                if theta1 == 0:
                    #turn 180
                    turn180(robot)
                    mov30(robot,end)
                elif theta1 == 1:
                    #turn right
                    turnRight(robot)
                    mov30(robot,end)
                elif theta1 == 2:
                    mov30(robot,end)
                else:
                    #turn left
                    turnLeft(robot)
                    mov30(robot,end)
            elif theta2 == 1:
                if theta1 == 0:
                    #turn left
                    turnLeft(robot)
                    mov31(robot,end)
                elif theta1 == 1:
                    #turn 180
                    turn180(robot)
                    mov31(robot,end)
                elif theta1 == 2:
                    #turn right
                    turnRight(robot)
                    mov31(robot,end)
                else:
                    mov31(robot,end)
            else:
                if theta1 == 0:
                    mov32(robot,end)
                elif theta1 == 1:
                    #turn left
                    turnLeft(robot)
                    mov32(robot,end)
                elif theta1 == 2:
                    #turn 180
                    turn180(robot)
                    mov32(robot,end)
                else:
                    #turn right
                    turnRight(robot)
                    mov32(robot,end)
    print('end',robot)