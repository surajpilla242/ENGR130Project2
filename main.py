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

#forward function
def move_forward():    
    powerSetting = [35,0]    # list of power settings, in pct, to cycle through
    for pwr_sig in powerSetting:
        r.motor(M1A,-1*pwr_sig)
        r.motor(M2B,1.1*pwr_sig)
        print("Power signal = {}".format(pwr_sig))
        sleep(1600) 

""" with open('test.txt', 'r') as file:
  lines = [line.strip() for line in file.readlines()]
  
for i in range(6)
    for j in range(9)
      if lines[i][j] == 'G'
        x_goal = i
        y_goal = j
"""
def wavefrontSearch():
    current_wave = 2
    found_wave = True
    while found_wave:
        found_wave = False
        for y in range(y_size):
            for x in range(x_size):
                if grid_map[x][y] == current_wave:
                    found_wave = True
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<x_size and 0<=ny<y_size:
                            if grid_map[nx][ny] == 0:
                                grid_map[nx][ny] = current_wave + 1
        current_wave += 1
        time.sleep_ms(500)  

def navigateToGoal():
    robot_pos = None
    for x in range(x_size):
        for y in range(y_size):
            if grid_map[x][y] == 99:
                robot_pos = (x, y)
                break
        if robot_pos: break
    
    current_dir = 0  # 0=North,1=East,2=South,3=West
    x, y = robot_pos
    
    while True:
        min_val = 99
        next_dir = current_dir
        next_pos = (x, y)
        
        for dir, (dx, dy) in enumerate([(0,1),(1,0),(0,-1),(-1,0)]):
            nx, ny = x+dx, y+dy
            if 0<=nx<x_size and 0<=ny<y_size:
                if grid_map[nx][ny] < min_val and grid_map[nx][ny] >=2:
                    min_val = grid_map[nx][ny]
                    next_pos = (nx, ny)
                    next_dir = dir
        
        dir_diff = (next_dir - current_dir) % 4
        if dir_diff == 1:
            turnRight90()
        elif dir_diff == 3:
            turnLeft90()
        elif dir_diff == 2:
            turnRight90()
            turnRight90()
            
        moveForward(1)
        x, y = next_pos
        current_dir = next_dir
        
        if grid_map[x][y] == 2:
            break
            
time.sleep(1000)
wavefrontSearch()
navigateToGoal()

while True:
    time.sleep(1000)
