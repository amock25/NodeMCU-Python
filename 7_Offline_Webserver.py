#####################################################################
						Shreejicharan Electronics
#####################################################################

import socket      #import socket module from firmware
import machine     #import machine module from firmware
import network     #import network module form firmware
import time        #import time module from firmware

#HTML code to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title> Offline Webserver </title> </head>
<center><h2>A simple webserver for turning LED  on and off using Micropython</h2></center>
<center><h3> Also IoT based Home Automation Shreejicharan Electronics </h3></center>
<form>
LED0: 
<button name="LED" value="ON0" type="submit">LED ON</button>
<button name="LED" value="OFF0" type="submit">LED OFF</button><br><br>
LED2: 
<button name="LED" value="ON2" type="submit">LED ON</button>
<button name="LED" value="OFF2" type="submit">LED OFF</button>
</form>
</html>
"""

#function for wifi station
def wifi_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('SCE', '12345678')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    print("hi")
   
   

wifi_connect()


#Setup PINS
LED0 = machine.Pin(16, machine.Pin.OUT)
LED2 = machine.Pin(2, machine.Pin.OUT)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.43.13', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    LEDON0 = request.find('/?LED=ON0')
    LEDOFF0 = request.find('/?LED=OFF0')
    LEDON2 = request.find('/?LED=ON2')
    LEDOFF2 = request.find('/?LED=OFF2')


    if LEDON0 == 6:
        print('TURN LED0 ON')
        LED0.off()
    if LEDOFF0 == 6:
        print('TURN LED0 OFF')
        LED0.on()
    if LEDON2 == 6:
        print('TURN LED2 ON')
        LED2.off()
    if LEDOFF2 == 6:
        print('TURN LED2 OFF')
        LED2.on()
    response = html
    conn.send(response)
    conn.close()
