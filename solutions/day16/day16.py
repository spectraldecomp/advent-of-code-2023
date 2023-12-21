import numpy as np
import sys
lines = open('solutions/day16/input.txt').read().splitlines()
arr = np.array([list(line) for line in lines])
sys.setrecursionlimit(1000000)



def run_laser(row, col, direction):
    visited = {(row, col): [] for row in range(arr.shape[0]) for col in range(arr.shape[1])}
    energized = set()
    laser(row, col, direction, visited, energized)
    return len(energized)

def laser(row, col, direction, visited, energized):
    if direction in visited[(row, col)]:
        return
    visited[(row, col)].append(direction)
    energized.add((row, col))
    if arr[row][col] == '/':
        map = {'up': 'right', 'right': 'up', 'down': 'left', 'left': 'down'}
        direction = [map[d] for d in direction]
    elif arr[row][col] == '\\':
        map = {'up': 'left', 'left': 'up', 'down': 'right', 'right': 'down'}
        direction = [map[d] for d in direction]
    elif arr[row][col] == '|':
        if 'left' in direction or 'right' in direction:
            direction = ['up', 'down']
    elif arr[row][col] == '-':
        if 'up' in direction or 'down' in direction:
            direction = ['left', 'right']
    for d in direction:
        if d == 'up' and row-1 >= 0:
            laser(row-1, col, ['up'], visited, energized)
        elif d == 'down' and row+1 < arr.shape[0]:
            laser(row+1, col, ['down'], visited, energized)
        elif d == 'left' and col-1 >= 0:
            laser(row, col-1, ['left'], visited, energized)
        elif d == 'right' and col+1 < arr.shape[1]:
            laser(row, col+1, ['right'], visited, energized)
    return

max_num = 0
for i in range(arr.shape[0]):
    num = run_laser(i, 0, ['right'])
    max_num = max(max_num, num)
for i in range(arr.shape[0]):
    num = run_laser(i, arr.shape[1]-1, ['left'])
    max_num = max(max_num, num)
for i in range(arr.shape[1]):
    num = run_laser(0, i, ['down'])
    max_num = max(max_num, num)
for i in range(arr.shape[1]):
    num = run_laser(arr.shape[0]-1, i, ['up'])
    max_num = max(max_num, num)
    
print(max_num)



            