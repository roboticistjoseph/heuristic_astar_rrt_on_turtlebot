# Path Planning using Hybrid RRT-A* algorithm and Case Study
> This repo brings you robust, optimal path planning for non-holonomic mobile robots (TurtleBot3) using RRT-A* and Informed RRT*—tested in both 2D and Gazebo. Follow the steps below to get rolling!
- For more details and project breakdown, please check out my blog: [link](https://josephkatakam.vercel.app/projects/nav_hybrid_rrt)
---

### 🚦 Step 1: Pre-Requisites

- **Ubuntu 18.04**
- **ROS Melodic**
- **Gazebo 9.1**
- **Turtlebot3 Packages**

---

### 🧰 Step 2: Check for Python Libraries

Make sure you have these installed (use `pip` or `apt` as needed):

```python
import numpy
import matplotlib.patches
import math
import rospy
import time
import heapq
import random
import sys
import pygame
```

---

### 🛠️ Step 3: Installing TurtleBot3 Packages

```bash
mkdir -p planning_ws/src
cd planning_ws
catkin_make
source devel/setup.bash

# Clone TurtleBot3 repositories
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git src/turtlebot3
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git src/turtlebot3_msgs
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git src/turtlebot3_simulations

cd ..
catkin_make
```

---

### 🚀 Step 4: Running the Package

1. **Download the package:**  
   Place `project_5` in your `planning_ws/src` directory.

2. **Build the package:**  
   ```bash
   catkin_make
   ```

3. **Source your workspace:**  
   ```bash
   source devel/setup.bash
   ```

4. **Set the TurtleBot3 model:**  
   ```bash
   export TURTLEBOT3_MODEL=burger
   ```

5. **Make the node executable:**  
   ```bash
   cd src/project_5/nodes
   chmod +x task
   ```

6. **Launch the node and Gazebo environment:**  
   ```bash
   roslaunch project_5 proj.launch
   ```

7. **Configure at runtime:**  
   - Enter **clearance** value (recommended: `0.03` to `0.07`)
   - Enter **RPM** value when prompted (suggested: `10`)

8. **Watch the magic:**  
   - The node will initialize in a few seconds.
   - TurtleBot3 will autonomously navigate to the goal in about a minute.

---

### 🏁 That’s it!

You’re all set to explore optimal path planning with RRT-A* and Informed RRT* on your TurtleBot3. For troubleshooting or more details, check the code comments and documentation.

---

> **Pro Tip:**  
> Tweak the clearance and RPM values to see how your TurtleBot3 handles different environments and constraints!

---

**Happy path planning!** 🚗💨

