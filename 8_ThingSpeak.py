#####################################################################
						Shreejicharan Electronics
#####################################################################

import usocket as _socket             #import usocket as _socket
from machine import ADC               #import ADC module from machine module from firmware
import ussl as ssl                    #import ssl module from firmware
import network                        #import network module from firmware 
import time                           #import time module from firmware

#function for identify wifi
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('SCE', '12345678')

temp = 0 

#API_KEY for Write & HOST as www.thingspeak.com
API_KEY = "50N88RBW1Z8B45XZ"  
HOST = "api.thingspeak.com"


#takes the value from sensor and send it to HOST
while True:

    #sense the Data from the sensor
    adc = ADC(0)
    temp = adc.read()
    #temp = temp * 0.48828125 #Disable comment in case of LM35 temperature sensor

    #Send the data to the HOST 
    data = b"api_key="+ API_KEY + "&field1=" + str(temp)   
    s = _socket.socket()
    ai = _socket.getaddrinfo(HOST, 443)        #Connecting to the HOST
    addr = ai[0][-1]
    s.connect(addr)
    s = ssl.wrap_socket(s)
    s.write("POST /update HTTP/1.0\r\n")
    s.write("Host: " + HOST + "\r\n")
    s.write("Content-Length: " + str(len(data)) + "\r\n\r\n")
    s.write(data)
    print(s.read(128))
    s.close()
    time.sleep(60)
        
