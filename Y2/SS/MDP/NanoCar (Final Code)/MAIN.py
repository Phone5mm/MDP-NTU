from tryDect import Detect
from btconnection import *
from RobotMove import *
from hamiltonianPath import shortestPath
from pathNavigation import move

if __name__ == '__main__':
 try:
  while True:

   stringdata = RECEIVE()
   print(stringdata)
   #if len(stringdata) == 0: break
   if (stringdata == "AUTO"):
    print("Running auto....")
    stringdata = RECEIVE()
   # if len(stringdata) == 0: break
    s = stringdata.split(",")
    temp = []
    ob_list = []
    count = 0
    for i in range (len(s)):
     if s[i].isnumeric():
      num = int(s[i])
      temp.append(num)
      count +=1
      if count == 3:
       ob_list.append(temp.copy())
       count = 0
       temp.clear()
     else: pass
    print("Obstacles list received = ", ob_list)

   #running auto program
    robot = [0,0,0]
    hamiltonianPath = shortestPath(ob_list)
    print("Shortest path", hamiltonianPath)
    for i in range (0, len(hamiltonianPath)):
     obstacle_id, imageid = move(robot, hamiltonianPath[i])
     sendMessage = "I:"+obstacle_id+","+str(imageid)
     print("Obstacle ID: ", obstacle_id)
     SEND(sendMessage)
     print("obstacle & image ID: ",sendMessage)
   if (stringdata == "MANUAL"):
    print("Running manual....")
   if (stringdata == "w"):
    FORWARD()
   if (stringdata == "s"):
    REVERSE()
   if (stringdata == "a"):
    TURNL()
   if (stringdata == "d"):
    TURNR()
   if (stringdata == "c"):
    m =0
    detect = Detect()
    id = detect.main(m)
    sendID = "I:" + str(id)
    SEND(sendID)
    print("Image detected is ", sendID)
   else: pass

 except IOError:
  pass

 CLOSE()
