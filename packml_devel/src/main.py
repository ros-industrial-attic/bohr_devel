#!/usr/bin/env python
#
# Software License Agreement (BSD License)
#
# Copyright 2017, Advanced Remanufacturing and Technology Centre
# Copyright 2017, Southwest Research Institute
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of the Southwest Research Institute, nor the names
#    of its contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

import rospy
import smach
import smach_ros

from resettingState import Resetting
from stoppedState import Stopped
from idleState import Idle
from startingState import Starting
from executeState import Execute
from stoppingState import Stopping

        
      
def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['outcome4'])
    sm.userdata.sm_counter = 0
    sm.userdata.sm_input = True
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


if __name__ == '__main__':
    main()
