#####################################################################
						Shreejicharan Electronics
#####################################################################

import machine                  #import machine module from firmware
import time                     #import time module from firmware

LED = machine.Pin(2, machine.Pin.OUT)  #Initialize GPIO2 as D4 on board

#do infinetely
while True:
    LED.on()             #pin status ON
    time.sleep(0.1)      #time delay of 0.1 second
    LED.off()            #pin status OFF
    time.sleep(0.1)      #time delay of 0.1 second

