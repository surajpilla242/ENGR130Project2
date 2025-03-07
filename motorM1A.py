# Example of controlling one of the motor ports on the robotbit
# Description:  basic API calls to control the speed of a DC motor

from microbit import *
import robotbit_library as r

# port definitions.
M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4

# Motor drive test
display.show("M")
r.setup()     # Set up the robobit
while True:
    powerSetting = [-100,-50,0,50,100]    # list of power settings, in pct, to cycle through
    for pwr_sig in powerSetting:
        r.motor(M1A,pwr_sig)
        print("Power signal = {}".format(pwr_sig))
        sleep(2000)    
   
