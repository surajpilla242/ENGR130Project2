from microbit import *
import math
import robotbit_library as r 

# Port definitions
M1A = 0x1  # Right motor
M2B = 0x4  # Left motor

# Sets up the robotbit
r.setup()

x_size = 10
y_size = 5
grid_map = [
    [0,0,0,0,0],
    [0,1,99,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,2,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

#left 90 turn function
def turnLeft90():
    r.motor(M1A,100) #right motor
    r.motor(M2B,100) #left motor
    sleep(250) #duration of turn (0.25 sec)
    r.motor(M1A,0) #stop right motor
    r.motor(M2B,0) #stop left motor

#right 90 turn function
def turnRight90():
    r.motor(M1A,-100) #right motor
    r.motor(M2B,-100) #left motor
    sleep(250) #duration of turn (0.25 sec)
    r.motor(M1A,0) #stop right motor
    r.motor(M2B,0) #stop left motor

#forward function
def moveForward():
    powerSetting = [35,0]    # list of power settings, in pct, to cycle through
    for pwr_sig in powerSetting:
        r.motor(M1A,-1*pwr_sig)
        r.motor(M2B,1.1*pwr_sig)
        print("Power signal = {}".format(pwr_sig))
        sleep(1600)    

while True:
    turnLeft90()
    sleep(5000) #pause for 5 seconds 
    turnRight90()
    sleep(5000) #pause for 5 seconds 
    moveForward()
    sleep(5000) #pause for 5 seconds 

    
    


