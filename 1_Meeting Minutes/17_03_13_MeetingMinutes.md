# ROS-Industrial PackML Meeting Notes
<b>Date:</b> 13th March 2017

<b> Attendees: </b>
- 3M: Lex Sackett
- ROS-I AP: Min Ling Chan, Mingli Han

<b>Apologies /Tentative:</b>
- 3M: Tom Strey
- PlusOne Robotics: Shaun Edwards
- SwRI: Paul Hvass 
- Gavin Hood

<b>Status Update:</b>

Mingli – ROS programming
- Computer ping from Mingli PC to PLC PC works 
- Connection issues with PLC and PC


**Update 14Mar Next Steps:**
- 3M:
   - Update Firmware on Siemens PLC
   - Ensure OPC-UA is enabled on PLC
 - Mingli
    - attempt to connect to PLC
    
 **Update 13Mar Next Steps:**   
 3M: Tom
 - Check if PLC is running as a server (server program)
 - Lex confirms PLC can not run as a server
   
   OPC-UA: 
   - Changed IP address to PLC (unable to connect) --> Mingli to try this again
   - Changed IP address to PC (working)
   - OPC connection goes to PLC --> needs to be working
   - PLC might not be exporting the OPC-UA correctly
   - Is the vendor PC running a Siemens software that can check the OPC-UA connection to the PLC? 
   - Run python on the vendor PC command line - but this wasn't working
   - Might need to enable OPC-UA connection on the vendor PC
   - Assume Ubuntu has been set up on Vendor PC ?
    
   
 Tom to check with vendor the following:
 - Does the PLC need to run a server program, in order to let the client (PC) to connect
      with it. Because that is the way we normally do. If yes, how to let the
      PLC run a server code/program?
  - Is there any PLC software installed on the PC that is able to control/communicate with
      PLC? If not, is there any other way we can test to confirm the PLC is
      connected with PC and able to communicate?
