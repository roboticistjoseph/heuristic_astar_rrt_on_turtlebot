# heuristic_rrt_on_turtlebot

-----------------------------------------------------------------------------------------------------------------
ENPM 661- Planning for Autonomous Robots;
-----------------------------------------------------------------------------------------------------------------

Name: Joseph Pranadeer Reddy Katakam
UID: 117517958

Name: Bharadwaj Chukkala
UID: 118341705

----------------------------------------------------------------------------------------------------------------

Project 5 Phase 2: Path Planning for a non-holonomic mobile robot in an obstacle space using A* and RRT

GitHub Link: https://github.com/roboticistjoseph/heuristic_rrt_on_turtlebot

Video Drive Link: https://drive.google.com/drive/folders/1JhDIIFGlIPOOEg2e1zyCKsxo-PngwNvd?usp=sharing

-----------------------------------------------------------------------------------------------------------------

####### How to run the package #########

Step 1: Pre Requisites

	--> Ubuntu 18.04
	--> ROS Melodic
	--> Gazebo 9.1
	--> Turtlebot3 Packages

------------------------------------------------------------------------------------------
Step 2: Check for libraries

	--> import numpy
	--> import matplotlib.patches
	--> import math
	--> import rospy
	--> import time
	--> import heapq
	--> import random
	--> import sys
	--> import pygame

------------------------------------------------------------------------------------------
Step 3: Installing Turtlebot Package (paste the following commands line by line)
	
	--> mkdir planning_ws/src
	--> catkin_make
	--> source devel/setup.bash
	--> git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
	--> git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
	--> git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
	--> cd  ../ && catkin_make

-------------------------------------------------------------------------------------------
Step 4: Running the package
	
	--> Download the package project_5 and paste it in your workspace.
	--> build the package using 'catkin_make'
	--> source it 'source devel/setup.bash'
	--> Run "export TURTLEBOT3_MODEL=burger" in the Terminal
	--> make the node executable, by navigating into the 'nodes' folder and running the command 'chmod +x task'
	--> launch the node and gazebo environment using 'roslaunch project_5 proj.launch'
	--> give clearance by typing in a value between "0.03-0.07"
	--> upon prompting give RPMs (suggested value is 10)
	--> The node will start running in a couple of seconds
	--> The turtlebot  will move to the goal in a minute.
-----------------------------------------------------------

