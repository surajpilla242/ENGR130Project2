def navigateToGoal():
    robot_x, robot_y = None, None
    for x in range(x_size):
        for y in range(y_size):
            if grid_map[x][y] == 99: 
                robot_x, robot_y = x, y

    if robot_x is None or robot_y is None:
        print("Error: Robot position not found in the map.")
        return

    current_x, current_y = robot_x, robot_y
    current_low = 99

    while current_low > 2:
        current_low = 99
        next_x, next_y = current_x, current_y

        if current_x > 0 and 2 <= grid_map[current_x - 1][current_y] < current_low:
            current_low = grid_map[current_x - 1][current_y]
            next_x, next_y = current_x - 1, current_y
        if current_x < x_size - 1 and 2 <= grid_map[current_x + 1][current_y] < current_low:
            current_low = grid_map[current_x + 1][current_y]
            next_x, next_y = current_x + 1, current_y
        if current_y > 0 and 2 <= grid_map[current_x][current_y - 1] < current_low:
            current_low = grid_map[current_x][current_y - 1]
            next_x, next_y = current_x, current_y - 1
        if current_y < y_size - 1 and 2 <= grid_map[current_x][current_y + 1] < current_low:
            current_low = grid_map[current_x][current_y + 1]
            next_x, next_y = current_x, current_y + 1

        moveForward(1)
        current_x, current_y = next_x, next_y
        printWavefrontMap()
        time.sleep(500)
