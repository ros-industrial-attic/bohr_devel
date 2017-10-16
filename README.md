# bohr_devel
PackML State Machine developmental repo

**Package objective:** Develop a prototype PackML state machine implementation, including tagged messages, based on an existing state machine ROS library. Test the prototype by communicating with at least one PLC running a standard PackML state machine.

PackML state machine implementation with smach state machine in ROS library

Bohr: Danish physicist https://en.wikipedia.org/wiki/Niels_Bohr

## Prerequisite
 Enable OPC UA server in the PLC firmware

## Installation
   * Cd into the `src` directory of your catkin workspace and run the following to create a ROS package

     `catkin_create_pkg package_name rospy smach`

   * Clone all the source files to `your_catkin_workspace/src/package_name/src`

   * In `your_catkin_workspace/src/package_name/src`, make the following files executable
     ```
     chmod +x main.py
     chmod +x client_rosmaster.py
     chmod +x cmd_Reset.py
     chmod +x cmd_Start.py
     chmod +x cmd_Stop.py
     ```

   * In `your_catkin_workspace`, run

     `catkin_make`
     
     `source devel/setup.bash`

   * Install smach_viewer by running the following
   
     `sudo apt-get install ros-indigo-smach-viewer`


## Applications
   * Demo PLC as PackML Master

     `rosrun package_name main.py`


   * Demo ROS as PackML Master

     Run the following to check the status of the current state in PLC
   
     `rosrun package_name clien_rosmaster`

     If the stopped state is True, run the following to give reset command to PLC
   
     `rosrun package_name cmd_Reset.py`
   
     The terminal will show Idle state goes to True
  
     If Idle state is true, run the following to give start command to PLC

     `rosrun package_name cmd_Start.py`

     The terminal will show that states of Starting, Execute, Completing and Complete will go to True sequentially

     If Complete state is True, run the following to give stop command

     `rosrun package_name cmd_Stop.py`

     The terminal will show that the Stopped state will go to True

## Reference
   Pure Python OPC-UA Client and Server https://github.com/FreeOpcUa/python-opcua
   
