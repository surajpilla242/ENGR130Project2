# Sample code to test the robotbit drivers for servos
# Description: The routine cycles through various angle settings of the
# standard servo

from microbit import *
import robotbit_library as r
# Define ports for the band of high current output S1-8
S1 = 0x1 # used for standard servo in this example
S2 = 0x2
S3 = 0x3
S4 = 0x4
S5 = 0x5
S6 = 0x6
S7 = 0x7
S8 = 0x8

r.setup()      # set up the robotbit
display.show("S")   # put message to LEDs at start up

while True:
# Cycle through a list of different angels setting to see how to control
# motion of the standard servo.
    angleSetting = [180, 0, 90]
    for angle in angleSetting:
        r.servo(S1, angle)
        print("angle = {}".format(angle))
        sleep(500)      # pause for 1/2 second to see position change