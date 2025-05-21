# header files
from utils import *
import sys


startCol = float(input("Enter the x-coordinate for start node : "))
startRow = float(input("Enter the y-coordinate for start node : "))
startOrientation = float(input("Enter the orientation for start node : "))
goalCol = float(input("Enter the x-coordinate for goal node : "))
goalRow = float(input("Enter the y-coordinate for goal node : "))
radius = float(input("Enter the radius of the rigid robot : "))
clearance = float(input("Enter the clearance of the rigid robot : "))
stepSize = float(input("Enter the step size : "))

# take start and goal node as input
start = (startRow, startCol, startOrientation)
goal = (goalRow, goalCol)
'''
astar = AStar(start, goal, clearance, radius, stepSize)

if(astar.IsValid(start[0], start[1])):
    if(astar.IsValid(goal[0], goal[1])):
        if(astar.IsObstacle(start[0],start[1]) == False):
            if(astar.IsObstacle(goal[0], goal[1]) == False):
                (explored_states, backtrack_states, distance_from_start_to_goal) = astar.search()
                astar.animate(explored_states, backtrack_states, "./astar_rigid.avi")
                
                print(len(explored_states))
                print(len(backtrack_states))

                # print optimal path found or not
                if(distance_from_start_to_goal == float('inf')):
                    print("\nNo optimal path found.")
                else:
                    print("\nOptimal path found. Distance is " + str(distance_from_start_to_goal))
            else:
                print("The entered goal node is an obstacle ")
                print("Please check README.md file for running Astar_rigid.py file.")
        else:
            print("The entered start node is an obstacle ")
            print("Please check README.md file for running Astar_rigid.py file.")
    else:
        print("The entered goal node outside the map ")
        print("Please check README.md file for running Astar_rigid.py file.")
else:
    print("The entered start node is outside the map ")
    print("Please check README.md file for running Astar_rigid.py file.")
'''
