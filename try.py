import math
from microbit import *  
import robotbit_library as r
import car_rec_motor
import car_send_motor

M1A = 0x1 
M2B = 0x4  

r.setup()

x_size = 10
y_size = 5

grid_map = [
    [0,  0,  0,  0,  0],
    [0,  1, 99,  1,  0],
    [0,  1,  1,  1,  0],
    [0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0],
    [0,  0,  2,  0,  0],
    [0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0]
]

def turnLeft90():
    r.motor(M1A, 100)
    r.motor(M2B, 100)
    sleep(250)  # 250 ms
    r.motor(M1A, 0)
    r.motor(M2B, 0)

def turnRight90():
    r.motor(M1A, -100)
    r.motor(M2B, -100)
    sleep(250) 
    r.motor(M1A, 0)
    r.motor(M2B, 0)

def moveForward(numBlocks):
    powerSetting = [35, 0]
    for pwr_sig in powerSetting:
        # Right motor negative for forward, left motor positive
        r.motor(M1A, -pwr_sig)
        r.motor(M2B, int(1.1 * pwr_sig))
        print("Power signal =", pwr_sig)
        sleep(1600) 

def wavefrontSearch():
    display.scroll('wfs')
    start_x, start_y = None, None
    for x in range(x_size):
        for y in range(y_size):
            if grid_map[x][y] == 99:
                start_x, start_y = x, y
                break
        if start_x is not None:
            break

    current_wave = 2
    found_wave = True

    while found_wave:
        found_wave = False
        for x in range(x_size):
            for y in range(y_size):
                if grid_map[x][y] == current_wave:
                    found_wave = True
                    if x > 0 and grid_map[x-1][y] == 0:
                        grid_map[x-1][y] = current_wave + 1
                        
                    if x < x_size - 1 and grid_map[x+1][y] == 0:
                        grid_map[x+1][y] = current_wave + 1
                        
                    if y > 0 and grid_map[x][y-1] == 0:
                        grid_map[x][y-1] = current_wave + 1
                        
                    if y < y_size - 1 and grid_map[x][y+1] == 0:
                        grid_map[x][y+1] = current_wave + 1
        current_wave += 1
        sleep(300)  
        if start_x is not None and start_y is not None:
        grid_map[start_x][start_y] = 99

def navigateToGoal():
    display.scroll('ntg')
    robot_pos = None
    for x in range(x_size):
        for y in range(y_size):
            if grid_map[x][y] == 99:
                robot_pos = (x, y)
                break
        if robot_pos is not None:
            break

    if robot_pos is None:
        raise ValueError("Could not find start (99) in grid_map")

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir = 0  
    x, y = robot_pos

    while True:
        if grid_map[x][y] == 2:
            print("Reached the goal:", x, y)
            break
        
        min_val = float('inf')
        next_dir = current_dir
        next_pos = (x, y)

        for d in range(4):
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            if 0 <= nx < x_size and 0 <= ny < y_size:
                val = grid_map[nx][ny]
                if val >= 2 and val < min_val:
                    min_val = val
                    next_pos = (nx, ny)
                    next_dir = d

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

sleep(1000)         
wavefrontSearch()    
navigateToGoal()    

while True:
    sleep(1000)      
