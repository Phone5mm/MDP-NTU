from hamiltonianPath import shortestPath 
from pathNavigation import move

if __name__ == "__main__":
    
    robot = [0,0,0.5]
    #Five obstacles and origin get from android
    obstacle_android = [[3,5,0],[3,9,0],[6,3,0],[15,10,0],[10,5,0]]
    hamiltonianPath = shortestPath(obstacle_android)
    print(hamiltonianPath) #hamiltonian Path
    for i in range(0, len(hamiltonianPath)): #Path Navigation
        move(robot,hamiltonianPath[i])
        print('obstacle coordinate: ', hamiltonianPath[i])
