from microbit import *
import radio
import robotbit_library as r
def move_forward:
    r.setup()
# Define Ports for the bank of high current output
# port definitions.
    M1A = 0x1
    M1B = 0x2
    M2A = 0x3
    M2B = 0x4
    
    # Motor drive test
    display.show("M")
         # Set up the robobit
    
    powerSetting = [35,0]    # list of power settings, in pct, to cycle through
    for pwr_sig in powerSetting:
        r.motor(M1A,-1*pwr_sig)
        r.motor(M2B,1.1*pwr_sig)
        print("Power signal = {}".format(pwr_sig))
        sleep(1600)    
       
