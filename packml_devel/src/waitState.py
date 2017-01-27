#!/usr/bin/env python

import roslib; roslib.load_manifest('test')
import rospy
import smach
import smach_ros

import time
import sys, os


        

# define state Wait
class Wait(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome1','outcome2'],
                             input_keys=['wait_in'],
                             output_keys=['wait_out'])
        
    def execute(self, userdata):
        rospy.loginfo('Executing state Wait')
        
        i = 0 # waiting time
        if userdata.wait_in == True:
           userdata.wait_out = True
           print("Terminate the PackML state machine after 5 seconds")
           while 1:
                  time.sleep(1)
                  i = i + 1
                  print(i)
                  if i==6:
                     break
           
           return 'outcome2'
    
        
