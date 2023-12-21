import numpy as np

def shift_row(row):
    next_stopper = 0
    rock_count = 0
    for i in range(len(row))[::-1]:
        if row[i] == 'O':
            row[i] = '.'
            rock_count += 1
        if row[i] == '#':
            next_stopper = i
            for j in range(rock_count):
                row[next_stopper + j + 1] = 'O'
            rock_count = 0
        if i == 0:
            next_stopper = i
            for j in range(rock_count):
                row[next_stopper + j] = 'O'
                
def cycle(arr):
    # North
    arr = arr.transpose()
    for row in arr:
        shift_row(row)
    arr = arr.transpose()
    
    # West
    for row in arr:
        shift_row(row)
    
    # South
    arr = arr.transpose()
    for row in arr:
        shift_row(row[::-1])
    arr = arr.transpose()
    
    # East
    for row in arr:
        shift_row(row[::-1])
    
def find_cycle(arr):
    arrs = []
    for i in range(1000000000):
        cycle(arr)
        for j, x in enumerate(arrs):
            if np.array_equal(arr, x):
                return j, i - j
        else:
            arrs.append(np.copy(arr))

def main():     
    lines = open('solutions/day14/input.txt').read().splitlines()
    arr = np.array([list(line) for line in lines])       
    copy_arr = np.copy(arr)

    offset, mod = find_cycle(arr)
    for i in range(offset + (1000000000 - offset) % mod):
        cycle(copy_arr)
    total_sum = 0
    for i, row in enumerate(copy_arr):
        num_rocks = sum(row == 'O') 
        total_sum += num_rocks * (len(copy_arr) - i)
    print(total_sum)
    
if __name__ == '__main__':
    main()
    