from microbit import *
import radio
import robotbit_library as r
# Define Ports for the bank of high current output
M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4

chnl = 03   #define channel to your team number

r.setup()

radio.config(channel=chnl)
radio.on()

def Drive(lft,rgt):
# Receive the percent power to drive each motor in a specific direction
    r.motor(M2B, lft)
    r.motor(M1A, rgt)

while True:
    s = radio.receive()                    # receive direction command
    if s is not None:
        if s=="N":                         # Drive forward 
            Drive(-90,90)
            display.show(Image.ARROW_N)
        elif s=="S":                       # Drive reverse 
            Drive(90,-90)
            display.show(Image.ARROW_S)
        elif s=="E":                       # Turn right
            Drive(-90,0)
            display.show(Image.ARROW_E)
        elif s=="W":                       # turn left
            Drive(0,90)
            display.show(Image.ARROW_W)
    else:
        Drive(0,0)
    sleep(20)

