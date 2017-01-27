#!/usr/bin/env python

import roslib; roslib.load_manifest('test')
import rospy
import smach
import smach_ros

from resetState import Reset 
from stoppedState import Stopped
from idleState import Idle
from waitState import Wait
        
      
def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['outcome4'])
    sm.userdata.sm_counter = 0
    sm.userdata.sm_input = True
    sm.userdata.sm_stopped_out = False
    sm.userdata.sm_reset_out = False
    sm.userdata.sm_idle_out = False

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('Stopped', Stopped(), 
                               transitions={'outcome1':'Reset', 
                                            'outcome2':'outcome4'},
                               remapping={'stopped_in':'sm_input', 
                                          'stopped_out':'sm_stopped_out'})
        smach.StateMachine.add('Reset', Reset(), 
                               transitions={'outcome1':'Idle',
                                            'outcome2':'outcome4'},
                               remapping={'reset_in':'sm_stopped_out',   #attach input data of state "Reset" to output data of state "Stopped"
                                          'reset_out':'sm_reset_out'})
        smach.StateMachine.add('Idle', Idle(),
                               transitions={'outcome1':'Wait',
                                            'outcome2':'outcome4'},
                               remapping={'idle_in':'sm_reset_out',     
                                          'idle_out':'sm_idle_out'})
        smach.StateMachine.add('Wait',Wait(),
                               transitions={'outcome1':'Stopped',
                                           'outcome2':'outcome4'},
                               remapping={'wait_in':'sm_idle_out'})


    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()
