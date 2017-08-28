#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright 2017, Advanced Remanufacturing and Technology Centre
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

from opcua import Client, ua
from opcua.ua import ua_binary as uabin
from opcua.common.methods import call_method
from opcua import common

import time

class HelloClient:
    def __init__(self, endpoint):
        self.client = Client(endpoint)

    def __enter__(self):
        self.client.connect()
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.disconnect()


if __name__ == '__main__':
    with HelloClient("opc.tcp://172.16.32.107:4840/freeopcua/server/") as client:


#--------------------------------
        ##Send Start Command
        cmdStart = client.get_node("ns=3;s=\"PackML_Status\".\"EM00\".\"Unit\".\"Cmd_Start\"")
        print("cmdStart was: ", cmdStart.get_value())
        print(" ") 
        print("Sending Start Command . . .")
        time.sleep(0.5)
        cmdStart.set_value(True)
        cmdStart_value = cmdStart.get_value()
        print("Cmd_Start is set to: ", cmdStart_value)

        time.sleep(5)
        ##Check Starting State
        starting_1 = client.get_node("ns=3;s=\"PackML_Status\".\"Sts\".\"State\".\"Starting\"")
        execute_1 = client.get_node("ns=3;s=\"PackML_Status\".\"Sts\".\"State\".\"Execute\"")
        completing_1 = client.get_node("ns=3;s=\"PackML_Status\".\"Sts\".\"State\".\"Completing\"")
        complete_1 = client.get_node("ns=3;s=\"PackML_Status\".\"Sts\".\"State\".\"Complete\"")
        
        starting_1_value = starting_1.get_value()
        print("Current Starting State: ", starting_1_value )
        time.sleep(2)
        execute_1_value =  execute_1.get_value()
        print("Current Execute State: ", execute_1_value)
        time.sleep(2)
        completing_1_value = completing_1.get_value()
        print("Current Completing State: ", completing_1_value)
        time.sleep(2)
        complete_1_value = complete_1.get_value()
        print("Current Complete State: ", complete_1_value)

        

