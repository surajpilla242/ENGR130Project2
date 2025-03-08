from microbit import *
import robotbit_library as r

# port definitions.
M1A = 0x1
M2B = 0x4

# sets up the robotbit
r.setup()     

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

turnLeft90()
sleep(5000) #pause for 5 seconds 
turnRight90()
