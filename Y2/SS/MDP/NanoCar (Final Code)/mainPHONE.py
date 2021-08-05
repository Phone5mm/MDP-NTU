from hamiltonianPath import shortestPath 
from pathNavigation import move
from RobotMove import *
import time

if __name__ == "__main__":

    robot = [0,0,0.5]
    #Five obstacles and origin get from android
    obstacle_android = [[3,5,0],[16,10,1.5]]
    hamiltonianPath = shortestPath(obstacle_android)
    print(hamiltonianPath) #hamiltonian Path
    for i in range(0, len(hamiltonianPath)): #Path Navigation
     move(robot,hamiltonianPath[i])
#     print("Obstacle ID" ,i)
