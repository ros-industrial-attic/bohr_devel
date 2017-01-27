The code in this package is for the developers to create PackML state machine using SMACH state machine in ROS library and make connection with at least one PLC running a standard PackML state machine.

The package is mainly used for progress update and discussion purpose. Currently, the developer is testing the data transition between different states. Input of a state becomes the output of another state. Stopped state, reset state, idle state and wait state are constructed for the initial test. In the following few weeks, more states will be constructed to simulate a typical work flow (diagram) of a PackML state machine. OPC UA python library will be used to test the connection with a remote PLC.


Instructions to run this package:
1. Create a catkin workspace ~/catkin_ws on a PC running Ubuntu and ROS
2. Create a package named 'packml_devel' in folder ~/catkin_ws/src
3. Copy the .py codes in this package to folder ~/catkin-ws/src/packml_devel/src
4. In ~/catkin-ws/src/packml_devel/src, run 
        Python main.py
