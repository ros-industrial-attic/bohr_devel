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

import sys
import logging
import time
import rospy
import smach
import smach_ros
import config

from resettingState import Resetting
from stoppedState import Stopped
from idleState import Idle
from startingState import Starting
from executeState import Execute
from stoppingState import Stopping

if __name__ == "__main__":
 
    # Connect PLC using PLC IP. 'client' is defined in config.py
    #client = Client("opc.tcp://172.16.32.107:4840/freeopcua/server/")
    config.client.connect()

    # Get ModuleActive tag to enable state machine
    var1 = config.client.get_node("ns=3;s=\"PackML_Status\".\"UN\".\"ModuleActive\"")
    moduleTag = var1.get_value()
 
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['outcome4'])
    
    # Define the input data of state machine, and let it equal to the value of ModuleActive tag 
    sm.userdata.sm_input = moduleTag 

    # Define the default output data of states
    sm.userdata.sm_stopped_out = False
    sm.userdata.sm_reset_out = False
    sm.userdata.sm_idle_out = False
    sm.userdata.sm_starting_out = False
    sm.userdata.sm_execute_out = False   

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('Stopped', Stopped(), 
                               transitions={'outcome1':'Reset', 
                                            'outcome2':'outcome4'},
                               remapping={'stopped_in':'sm_input', 
                                          'stopped_out':'sm_stopped_out'})
        smach.StateMachine.add('Reset', Resetting(), 
                               transitions={'outcome1':'Idle',
                                            'outcome2':'outcome4'},
                               remapping={'reset_in':'sm_stopped_out',   #attach input data of state "Resetting" to output data of state "Stopped"
                                          'reset_out':'sm_reset_out'})
        smach.StateMachine.add('Idle', Idle(),
                               transitions={'outcome1':'Starting',
                                            'outcome2':'outcome4'},
                               remapping={'idle_in':'sm_reset_out',     
                                          'idle_out':'sm_idle_out'})
        smach.StateMachine.add('Starting', Starting(),
                               transitions={'outcome1':'Execute',
                                            'outcome2':'outcome4'},
                               remapping={'starting_in':'sm_idle_out',
                                          'starting_out':'sm_starting_out'})
        smach.StateMachine.add('Execute', Execute(),
                               transitions={'outcome1':'Stopping',
                                            'outcome2':'outcome4'},
                               remapping={'execute_in':'sm_starting_out',
                                          'execute_out':'sm_execute_out'})
        smach.StateMachine.add('Stopping',Stopping(),
                               transitions={'outcome1':'Stopped',
                                           'outcome2':'outcome4'},
                               remapping={'stopping_in':'sm_execute_out'})

    # Create and start the introspection server
    sis = smach_ros.IntrospectionServer('packmlSmach', sm,'/SM_PACKML')
    sis.start()
    
    # Execute SMACH plan
    outcome = sm.execute()
 
    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()
    config.client.disconnect()


