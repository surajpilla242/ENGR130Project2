def printWavefrontMap():
    for y in reversed(range(y_size)): 
        print_row = ""
        for x in range(x_size):
            if grid_map[x][y] == 99:
                print_row += "R  "  
            elif grid_map[x][y] == 2:
                print_row += "G  "  
            elif grid_map[x][y] == 1:
                print_row += "X  "  
            elif grid_map[x][y] == '*':
                print_row += "*  "  
            else:
                print_row += f"{grid_map[x][y]:<3}"  
        print(print_row)
    print()
