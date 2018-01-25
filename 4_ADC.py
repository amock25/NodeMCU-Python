#####################################################################
						Shreejicharan Electronics
#####################################################################


import machine                 #import machine module from firmware
import time                    #import time module from firmware
adc = machine.ADC(0)           #define the analog pin as A0

#do infinitely
while True:
    
    dout=adc.read()           #read the data from the pin and save it
    print("Dout=", dout)      #print the sense data on serial monitor
    time.sleep(1)             #provide the time delay of 1 second
