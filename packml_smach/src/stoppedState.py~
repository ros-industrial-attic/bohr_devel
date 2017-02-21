#!/usr/bin/env python

import roslib; roslib.load_manifest('test')
import rospy
import smach
import smach_ros

# define steady state / stopped
class Stopped(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome1','outcome2'],
                             input_keys=['stopped_in'],
                             output_keys=['stopped_out'])

    def execute(self, userdata):
        rospy.loginfo('Executing state Stopped')
        if userdata.stopped_in == True:
            userdata.stopped_out = True
            
            return 'outcome1'
        else:
            return 'outcome2'
            

