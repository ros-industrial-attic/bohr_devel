#!/usr/bin/env python

import roslib; roslib.load_manifest('test')
import rospy
import smach
import smach_ros


        

# define state Idle
class Idle(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome1','outcome2'],
                             input_keys=['idle_in'],
                             output_keys=['idle_out'])
        
    def execute(self, userdata):
        rospy.loginfo('Executing state Idle')
        if userdata.idle_in == True:
           userdata.idle_out = True
           return 'outcome1'
        else:
           return 'outcome2'    
        
