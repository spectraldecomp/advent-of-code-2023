import numpy as np

lines = open('solutions/day10/input.txt').read().splitlines()

maze = np.array([list(line) for line in lines])



def find_s_location(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'S':
                return row, col
            
def find_path(path, row, col):
    if maze[row][col] == 'S':
        print("Found S")
        return path
    else:
        path.append((row, col))
    print("Recursing on " + str(row) + ", " + str(col), "path is currently " + str(path))
        
    # Go up first
    if maze[row-1][col] in ['|','7','F'] and (row-1, col) not in path:
        print("Going up")
        find_path(path, row-1, col)
    # Then down
    elif maze[row+1][col] in ['|','L','J'] and (row+1, col) not in path:
        print("Going down")
        find_path(path, row+1, col)
    # Then left
    elif maze[row][col-1] in ['-','L','F'] and (row, col-1) not in path:
        print("Going left")
        find_path(path, row, col-1)
    # Then right
    elif maze[row][col+1] in ['-','J','7'] and (row, col+1) not in path:
        print("Going right")
        find_path(path, row, col+1)
    # Deadend, go back
    print("Deadend, going back")
    return 
        
        

s_loc = find_s_location(maze)

path = find_path([], s_loc[0]+1, s_loc[1])
print(path)



