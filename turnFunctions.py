from microbit import *
import robotbit_library as r

# port definitions.
M1A = 0x1
M2B = 0x4

# sets up the robotbit
r.setup()     

#left 90 turn function
def turnRight90():
    powerSetting = [100,0]    # list of power settings, in pct, to cycle through
    for pwr_sig in powerSetting:
        r.motor(M1A, pwr_sig)
        r.motor(M2B, pwr_sig)
        sleep(250) 

#right 90 turn function
def turnLeft90():
   powerSetting = [-100,0]    # list of power settings, in pct, to cycle through
   for pwr_sig in powerSetting:
        r.motor(M1A, pwr_sig)
        r.motor(M2B, pwr_sig)
        sleep(250) 

turnLeft90()
sleep(5000) #pause for 5 seconds 
turnRight90()
