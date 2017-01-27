#!/usr/bin/env python

import roslib; roslib.load_manifest('test')
import rospy
import smach
import smach_ros


        

# define state Reset
class Reset(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome1','outcome2'],
                             input_keys=['reset_in'],
                             output_keys=['reset_out'])
        
    def execute(self, userdata):
        rospy.loginfo('Executing state Reset')
        if userdata.reset_in == True:
           userdata.reset_out = True
           return 'outcome1'
        else:
           return 'outcome2'    
        
        


