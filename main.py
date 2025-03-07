import math
import robotbit_library
import car_rec_motor
import car_send_motor
import ultrasonic_Grove

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

def moveForward(numBlocks):
    r.motor(M1A,-1*35) #right motor
    r.motor(M2B,1.1*35) #left motor
    duration = (25/(6.5*math.pi)) * 360 * numBlocks #calc sleep duration
    sleep(3*duration)
    r.motor(M1A,0) #stop right motor
    r.motor(M2B,0) #stop left motor

# Port definitions
M1A = 0x1  # Right motor
M2B = 0x4  # Left motor

# Sets up the robotbit
r.setup()


with open('test.txt', 'r') as file:
  lines = [line.strip() for line in file.readlines()]
  
for i in range(6)
    for j in range(9)
      if lines[i][j] == 'G'
        x_goal = i
        y_goal = j
