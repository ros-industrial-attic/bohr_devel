#ROS-Industrial PackML Meeting Notes
<b>Date:</b> 5th June 2017

<b>Attendees: </b>
- 3M: Tom Strey
- ROS-I AP: Min Ling Chan
- SwRI: Paul Evans, Matt R., Austin D.
- PlusOne Robotics: Paul Hvass
- Simul-Tech: Gavin

-<b>Apologies / Tentative:</b>
- 3M: Lex
- PlusOne Robotics: Shaun Edwards

<b>Status Update:</b>

-**Requirements to finalise PackML – Phase 1 Collaboration project** -Open items:

<b>- 1. RVIZ with statemachine – Austin </b>

- RVIZ - C++ library
  - Proto rviz plugin by end of this week
  - Timeframe:End of June
 
 - Provide screenshot or video of a test case - end of the meeting

<b>-2. C++ Library – Shaun Edwards </b>
- Tested on ROS hardware using PackML
- SC tags - check with Shaun Edwards.
- 17 states - check if all has been included in the C++ library
- Timeline: End of June

  - Check if within scope for PlusOne Robotics:
    -  Test with OPC-UA PLC --> not yet. 

<u>Feedback required:</u>

  - New OPC UA code written in C++ has been uploaded ? not too sure if it will work ? https://github.com/FreeOpcUa/freeopcua

<b>-3. SMACH Library - ARTC </b>
-  Beckhoff (OPC-UA) - to be tested by ARTC
- Timeframe: End June

<b>-4.PLC controllers - 3M </b>
- Info only:
- AB currently not OPC-UA --> expected coming soon
- Beckhoff is OPC-UA

-<b>Next Steps:</b>

-1. Mode Selection:　 This allows a piece of equipment to operate
- Require to test C++ with PLC
     - dependent on OPC-UA C++ library

-Next meeting will be held in 2 weeks, 3rd July.
