A = [30,50,0.5]
B = [150,150,0.5]
def move(start,end):
    robot = start
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    theta1 = start[2]
    theta2 = end[2]
    print('Origin',robot)
    if x2>x1 and y2>y1: #top right 
        print('Des is top right of robot')
        if x2-x1-20>0 and y2-y1-20>0:
            #turn right
            if robot[2] != 0:
                robot[2] = robot[2] - 0.5
            else:
                robot[2] = 1.5
            print('Turn right',robot)
            #go straight for x2-x1-20
            robot[0] = robot[0] + x2-x1-20
            print('Go straight',robot)
            #turn left
            if robot[2] != 1.5:
                robot[2] = robot[2] + 0.5
            else:
                robot[2] = 0
            print('Turn left',robot)
            #go straight for y2-y1-20
            robot[1] = robot[1] + y2-y1-20
            print('Go straight',robot)
    print(robot)
move(A,B)


