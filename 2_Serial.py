#####################################################################
						Shreejicharan Electronics
#####################################################################

from machine import UART   #import UART module from machine from firmware  
import time                #import time module from firmware

uart = UART(1, 9600)                         # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

while True:
    uart.write('abcdrtdtd')   # write the 3 characters
    time.sleep(1)             #provide time interval of 1 second
