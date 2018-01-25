#####################################################################
						Shreejicharan Electronics
#####################################################################

import machine,time, math                    #import machine, time & math module from firmware
led = machine.PWM(machine.Pin(2), freq=1000) #creat pwm object for pin 2 with frequency of 1000 hz

#define function as pulse
def pulse(l, t):
    for i in range(20):         
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500)) #set the duty cycle
        #l.duty(i)
        time.sleep_ms(t)

#do infinitely
while True:
    pulse(led, 50)       #
