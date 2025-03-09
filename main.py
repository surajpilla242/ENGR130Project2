import math
import robotbit_library
import car_rec_motor
import car_send_motor
import ultrasonic_Grove

# Port definitions
M1A = 0x1  # Right motor
M2B = 0x4  # Left motor

# Sets up the robotbit
r.setup()

TIME_OUT = 100000  # Increase time out to see farther, but
# this will reduce the sample rate
ECHO = pin1  # ping sensor uses a single pin for ECHO and Trigger
TRIGGER = pin1


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
def moveForward(numBlocks):
    r.motor(M1A,-1*35) #right motor
    r.motor(M2B,1.1*35) #left motor
    duration = (25/(6.5*math.pi)) * 360 * numBlocks #calc sleep duration
    sleep(3*duration)
    r.motor(M1A,0) #stop right motor
    r.motor(M2B,0) #stop left motor
    
#ultrasonic function
def distance(tp, ep):
    # tp is the trigger pin and ep is the echo pin
    ep.read_digital()  # clear echo
    tp.write_digital(1)  # Send a 10 microSec pulse
    sleep_us(10)  # wait 10 microSec
    tp.write_digital(0)  # Send pulse low
    ep.read_digital()  # clear echo signal - This is needed for a
    # pingSensor
    ts = time_pulse_us(ep, 1, TIME_OUT)  # Wait for echo or time out
    if ts > 0:
        ts = ts * 17 // 100  # if system did not timeout, then send
        # back a scaled value
    return ts  # Return timeout error as a negative number (-1)


with open('test.txt', 'r') as file:
  lines = [line.strip() for line in file.readlines()]
  
for i in range(6)
    for j in range(9)
      if lines[i][j] == 'G'
        x_goal = i
        y_goal = j
