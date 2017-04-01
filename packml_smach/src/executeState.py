#!/usr/bin/env python
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

import config




        

# define state Execute
class Execute(smach.State):
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['outcome1','outcome2'],
                             input_keys=['execute_in'],
                             output_keys=['execute_out'])
        
    def execute(self, userdata):
        rospy.loginfo('Executing state Execute')

        # Receive Stop Tag
        var = config.client.get_node("ns=3;s=\"PackML_Status\".\"UN\".\"Cmd_Stop\"")  
        var.set_value(True)
        config.stopTag = var.get_value()
        print("Received stop command: ", config.stopTag)
        if userdata.execute_in == True and config.stopTag == True:
           userdata.execute_out = True
           return 'outcome1'
        else:
           return 'outcome2'    
        
