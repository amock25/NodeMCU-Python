#####################################################################
						Shreejicharan Electronics
#####################################################################

import network         #import network module from firmware

#wifi as a stataion
def wifi_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('SCE', '12345678')   #ssid=SCE, Password=12345678
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())   
    print("Hello")

wifi_connect()
