import numpy as np

lines = open('solutions/day3/input.txt').read().splitlines()

def part1():
    # Convert lines to a 2d numpy array and pad with '.' to avoid checking for out of bounds
    matrix = np.array([list(line) for line in lines])
    matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values='.')
    rows, cols = matrix.shape
    sum = 0
    
    # Check each place in the matrix
    row = 1
    while row < rows:
        col = 1
        while col < cols:
            if matrix[row][col].isnumeric():
                # char is a number, check surrounding places
                checked_places = [matrix[row-1][col-1], matrix[row-1][col], matrix[row-1][col+1], matrix[row][col-1], matrix[row][col+1], matrix[row+1][col-1], matrix[row+1][col], matrix[row+1][col+1]]
                if not all(place in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] for place in checked_places):
                    # Not all surrounding places are numbers or '.', so this is a part number
                    # Get full number substring, i.e. check to the left and right and get all digits
                    left_start = -1
                    for j in range(col-1, -1, -1):
                        if matrix[row][j].isnumeric() and j == 1:
                            left_start = 1
                            break
                        if matrix[row][j].isnumeric():
                            continue
                        else: 
                            left_start = j+1
                            break
                    right_end = -1
                    for j in range(col+1, cols):
                        if matrix[row][j].isnumeric() and j == cols-2:
                            right_end = cols-2
                        if matrix[row][j].isnumeric():
                            continue
                        else:
                            right_end = j
                            break
                    number = int(''.join(matrix[row, left_start:right_end].tolist()))
                    sum += number
                
                    # Continue checking after the place of the last digit of the number
                    col = right_end
            col += 1
        row += 1
    print(sum)
    
def part2():
    # Convert lines to a 2d numpy array and pad with '.' to avoid checking for out of bounds
    matrix = np.array([list(line) for line in lines])
    matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values='.')
    rows, cols = matrix.shape
    sum = 0
    gears = {}
    # Check each place in the matrix
    row = 1
    while row < rows:
        col = 1
        while col < cols:
            if matrix[row][col].isnumeric():
                # char is a number, check surrounding places for a gear
                new_col = -1
                for i in range(row-1, row+2):
                    for j in range(col-1, col+2):
                        place = matrix[i][j]
                        if place == '*':
                            # record the coords of the gear
                            coords = (i, j)
                        
                            # Get full number substring, i.e. check to the left and right and get all digits
                            left_start = -1
                            for j in range(col-1, -1, -1):
                                if matrix[row][j].isnumeric() and j == 1:
                                    left_start = 1
                                    break
                                if matrix[row][j].isnumeric():
                                    continue
                                else: 
                                    left_start = j+1
                                    break
                            right_end = -1
                            for j in range(col+1, cols):
                                if matrix[row][j].isnumeric() and j == cols-2:
                                    right_end = cols-2
                                if matrix[row][j].isnumeric():
                                    continue
                                else:
                                    right_end = j
                                    break
                                
                            number = int(''.join(matrix[row, left_start:right_end].tolist()))
                            
                            # Add this number to gears
                            if coords in gears:
                                gears[coords].append(number)
                            else:
                                gears[coords] = [number]
                        
                            # Continue checking after the place of the last digit of the number
                            new_col = right_end
                if new_col != -1:
                    col = new_col
            col += 1
        row += 1
        
    # Multiply each entry of each gear together
    for gear in gears:
        if len(gears[gear]) == 2:
            gears[gear] = np.prod(gears[gear])
            sum+=gears[gear]
    print(sum)

part1()
part2()

