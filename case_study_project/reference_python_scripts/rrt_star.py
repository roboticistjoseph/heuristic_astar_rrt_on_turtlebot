# header files
from utils import *
import sys


startX = float(input("Enter the x-coordinate for start node : "))
startY = float(input("Enter the y-coordinate for start node : "))
goalX = float(input("Enter the x-coordinate for goal node : "))
goalY = float(input("Enter the y-coordinate for goal node : "))

# take start and goal node as input
start = (startX * 100.0, startY * 100.0)
goal = (goalX * 100.0, goalY * 100.0)
rrt = RRTStar(start, goal)

if(rrt.IsValid(start[0], start[1])):
    if(rrt.IsValid(goal[0], goal[1])):
        if(rrt.IsObstacle(start[0],start[1]) == False):
            if(rrt.IsObstacle(goal[0], goal[1]) == False):
                (explored_states, backtrack_states) = rrt.search()
                
                # animate the path
                rrt.animate(explored_states, backtrack_states)
                
                print(len(explored_states))
                print(len(backtrack_states))
            else:
                print("The entered goal node is an obstacle ")
                print("Please check README.md file for running rrt_star.py file.")
        else:
            print("The entered start node is an obstacle ")
            print("Please check README.md file for running rrt_star.py file.")
    else:
        print("The entered goal node outside the map ")
        print("Please check README.md file for running rrt_star.py file.")
else:
    print("The entered start node is outside the map ")
    print("Please check README.md file for running rrt_star.py file.")
