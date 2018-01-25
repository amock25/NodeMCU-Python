#####################################################################
						Shreejicharan Electronics
#####################################################################

from machine import Pin    #import pin module from machine from 
import time                #import time module from firmware

digitalSensor = Pin(2, Pin.IN, Pin.PULL_UP) ##Initialize GPIO2 as D4 as input mode

#do infinitely
while True:

    status = digitalSensor.value()    #read the sensor value from the pin and store it 
    print(status)                     #print the value of sensor value on serial monitor
    time.sleep(1)                     #provide time delay of 1 second
