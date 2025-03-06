from microbit import *
import radio
import robotbit_library as r

# Define Ports for the bank of high current output
M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4

def Drive(lft,rgt):
# Receive the percent power to drive each motor in a specific direction
    r.motor(M2B, lft)
    r.motor(M1A, rgt)

def turnLeft90():
  #distance one wheel must travel for 90 degree point turn = 8.6 cm
  # wheel circumference = 19.5 cm
    countsToTravel = ((8.6/17.6)/19.5)*(360)

  #encoder target for countsToTravel
    r.motor(M2B, 0)
    r.motor(M1A, 0)
    r.motor(M2B, countsToTravel)
    r.motor(M1A, countsToTravel)
    r.motor(M2B, 50)
    r.motor(M1A, -50)

#stop for half second at end of movement
    r.motor(M2B, 0)
    r.motor(M1A, 0)
    sleep(500)


