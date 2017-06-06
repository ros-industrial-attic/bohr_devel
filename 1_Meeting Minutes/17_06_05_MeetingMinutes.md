# ROS-Industrial PackML Meeting Notes<b>Date:</b> 13th March 2017
<b> Attendees: </b>
- 3M: Tom Strey
- ROS-I AP: Min Ling Chan

-<b>Apologies / Tentative:</b>
- 3M: Lex
- PlusOne Robotics: Shaun Edwards, Paul Hvass
- SwRI: Paul Evans
- Gavin Hood

<b>Status Update:</b>
-**Requirements to finalise PackML – Phase 1 Collaboration project**
-Open items:

-RVIZ with statemachine – Austin
 - Upload code on github
 - Provide screenshot or video of a test case
 - ARTC to run with PLC connected (note we only have this for another 5 days as it is on loan)

-C++ Python Library – Shaun Edwards
  - Progress with connection to OPC-UA 
  - New OPC UA code written in C++ has been uploaded ? not too sure if it will work ? https://github.com/FreeOpcUa/freeopcua
  - Test with OPC-UA PLC 

-<b>Next steps:</b>

-1. Mode Selection:　 This allows a piece of equipment to operate completely differently depending on "mode" selected. This is defined in the ISA-88 Standard
- Mode selection list (mode 1-5) each equipment module can operate different functions ("modes")
　-Ie: 
     - Mode 1 - workcell (locks out other modes)
     - Mode 2 - manual mode (testing, verification etc)
     - Mode 3 - Calibration - sensor or robot needs location calibration

     - Timeframe: 4-6 weeks
     - Software Developer: ARTC (Python) / PlusOne Robotics (C++)

-2. PackML State Times:　 This accumulates the amount of time that the packML master is in each state. 
- Develop this in python based on the  ladder logic provided by Tom. - ARTC
- C++ --> Shaun (has this been completed?)

- Review PLC standard ladder / PLC logic, convert the timers and other required logic where necessary to be used by ROS. - ARTC

-Next meeting will be held in 2 weeks, 19th June.

