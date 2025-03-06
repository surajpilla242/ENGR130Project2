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
 countsToTravel = ((167.7/17.6)/19.5)*(360)

  #encoder target for countsToTravel
    r.motor(M2B, 0)
    r.motor(M1A, 0)
    r.motor(M2B, countsToTravel)
    r.motor(M1A, countsToTravel)

  r.motor(0, 90)
  r.motor(0, 0)
  r.motor(countsToTravel, lft)
  r.motor(countsToTravel, rgt)
  r.motor(50, lft)
  r.motor(-50, rgt)
  #while(nMotorRunState[motorB] != runStateIdle && nMotorRunState[motorC] != runStateIdle) {}

  #stop for half second at end of movement
  r.motor(0, lft)
  r.motor(0, rgt)
  sleep(500)
