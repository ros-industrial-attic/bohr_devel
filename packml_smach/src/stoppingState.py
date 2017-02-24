#!/usr/bin/env python
#
#
# Software License Agreement (Apache License)
# Copyright (c) 2017, <Advanced Remanufacturing Technology Centre/Mingli Han>
 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
 
# http://www.apache.org/licenses/LICENSE-2.0
 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rospy
import smach
import smach_ros

import time
import sys, os


        

# define state Stopping
class Stopping(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome1','outcome2'],
                             input_keys=['stopping_in'],
                             output_keys=['stopping_out'])
        
    def execute(self, userdata):
        rospy.loginfo('Executing state Stopping')
        
        i = 0 # waiting time
        if userdata.stopping_in == True:
           userdata.stopping_out = True
           print("Stop the PackML state machine after 5 seconds by ctrl-c")
           while 1:
                  time.sleep(1)
                  i = i + 1
                  print(i)
                  if i==6:
                     break
           
           return 'outcome2'
    
        
