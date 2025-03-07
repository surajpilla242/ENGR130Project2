from microbit import *
import robotbit_library as r
import time

r.setup()
M1A = 0x1  
M2B = 0x4

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

def Drive(lft, rgt):
    r.motor(M2B, lft)
    r.motor(M1A, rgt)

def moveForward(blocks):
    Drive(-50, 50)  
    time.sleep_ms(500)
    Drive(0, 0)

def turnLeft90():
    Drive(40, 0) 
    time.sleep_ms(500)  
    Drive(0, 0)

def turnRight90():
    Drive(-40, 0)
    time.sleep_ms(500)
    Drive(0, 0)

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

display.show(Image.ARROW_N)
time.sleep(1000)
wavefrontSearch()
navigateToGoal()

while True:
    time.sleep(1000)
