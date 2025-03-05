import math
import robotbit_library
import car_rec_motor
import car_send_motor
import ultrasonic_Grove


with open('test.txt', 'r') as file:
  lines = [line.strip() for line in file.readlines()]
