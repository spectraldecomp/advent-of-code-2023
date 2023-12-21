import numpy as np
import sys
# So my CPU can more effectively light itself on fire
sys.setrecursionlimit(100000)

lines = open('solutions/day10/input.txt').read().splitlines()
maze = np.array([list(line) for line in lines])


# Finds the location of the starting point
def find_s_location(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'S':
                return row, col
       

# Recursively finds the path from the starting point to the end     
def find_path(path, row, col):
    path.append((row, col))
    if maze[row][col] == '|':
        if (row-1, col) not in path and maze[row-1][col] in ['|','7','F']:
            find_path(path, row-1, col)
        if (row+1, col) not in path and maze[row+1][col] in ['|','L','J']:
            find_path(path, row+1, col)
    if maze[row][col] == '-':
        if (row, col-1) not in path and maze[row][col-1] in ['-','L','F']:
            find_path(path, row, col-1)
        if (row, col+1) not in path and maze[row][col+1] in ['-','J','7']:
            find_path(path, row, col+1)
    if maze[row][col] == 'L':
        if (row-1, col) not in path and maze[row-1][col] in ['|','7','F']:
            find_path(path, row-1, col)
        if (row, col+1) not in path and maze[row][col+1] in ['-','J','7']:
            find_path(path, row, col+1)
    if maze[row][col] == 'J':
        if (row-1, col) not in path and maze[row-1][col] in ['|','7','F']:
            find_path(path, row-1, col)
        if (row, col-1) not in path and maze[row][col-1] in ['-','L','F']:
            find_path(path, row, col-1)
    if maze[row][col] == '7':
        if (row+1, col) not in path and maze[row+1][col] in ['|','L','J']:
            find_path(path, row+1, col)
        if (row, col-1) not in path and maze[row][col-1] in ['-','L','F']:
            find_path(path, row, col-1)
    if maze[row][col] == 'F':
        if (row+1, col) not in path and maze[row+1][col] in ['|','L','J']:
            find_path(path, row+1, col)
        if (row, col+1) not in path and maze[row][col+1] in ['-','J','7']:
            find_path(path, row, col+1)
    return

# Use ray casting to check if a point is inside the maze
def check_point(row, col):
    count = 0
    for i in range(0, col):
        #TL;DR: Weird edge case. If we have a sort of FJ or L7 shape, we get +2 count instead of +1. So we ignore the
        # F and 7 cases. Which doesn't hurt us because we either have FJ and L7 which are accounted for or we have
        # F7 and LJ which are congruent mod 2.
        if maze[row][i] in ['|', 'L', 'J'] and (row, i) in path:
            count += 1
    if count % 2 == 1:
        return True
    return False

# Check how many points are inside the maze
def check_points():
    count = 0
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if (row, col) not in path:
                if check_point(row, col):
                    count += 1
    return count
        
        

s_loc = find_s_location(maze)
path = []
find_path(path, s_loc[0], s_loc[1]+1)
print(len(path)/2 if len(path) % 2 == 0 else len(path)//2 + 1)
print(check_points())



