import numpy as np

lines = open('solutions/day3/input.txt').read().splitlines()

def part1():
    sum = 0
    # Convert lines to a 2d numpy array
    matrix = np.array([list(line) for line in lines])
    
    # Get the number of rows and columns
    rows, cols = matrix.shape
    
    # Check the first row
    for i in range(1, cols-1):
        isPartNumber = True
        if not matrix[0][i].isnumeric():
            continue
        elif matrix[0][i].isnumeric():
            # char is a number, check left, right, down, and diagonals
            checked_places = [matrix[0][i-1], matrix[0][i+1], matrix[1][i], matrix[1][i+1], matrix[1][i-1]]
            if all(place in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] for place in checked_places):
                isPartNumber = False
        if isPartNumber:
            print (matrix[0][i] + " is a number")
            # Get full number substring, i.e. check to the left and right and get all digits
            left_start = -1
            for j in range(i-1, -1, -1):
                if matrix[0][j].isnumeric() and j == 0:
                    left_start = 0
                    break
                if matrix[0][j].isnumeric():
                    continue
                else: 
                    left_start = j+1
                    break
            right_end = -1
            for j in range(i+1, cols):
                if matrix[0][j].isnumeric() and j == cols-1:
                    right_end = cols-1
                if matrix[0][j].isnumeric():
                    continue
                else:
                    right_end = j
                    break
            number = int(''.join(matrix[0, left_start:right_end].tolist()))
            sum += number
            
            # Continue checking after the place of the last digit of the number
            i = right_end
        
    
    # Check the last row
    for i in range(1, cols-1):
        isPartNumber = True
        if not matrix[rows-1][i].isnumeric():
            continue
        elif matrix[rows-1][i].isnumeric():
            # char is a number, check left, right, up, and diagonals
            checked_places = [matrix[rows-1][i-1], matrix[rows-1][i+1], matrix[rows-2][i], matrix[rows-2][i+1], matrix[rows-2][i-1]]
            if all(place in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] for place in checked_places):
                isPartNumber = False
        if isPartNumber:
            print (matrix[cols-1][i] + " is a number")
            # Get full number substring, i.e. check to the left and right and get all digits
            left_start = -1
            for j in range(i-1, -1, -1):
                if matrix[rows-1][j].isnumeric() and j == 0:
                    left_start = 0
                    break
                if matrix[rows-1][j].isnumeric():
                    continue
                else: 
                    left_start = j+1
                    break
            right_end = -1
            for j in range(i+1, cols):
                if matrix[rows-1][j].isnumeric() and j == cols-1:
                    right_end = cols-1
                if matrix[rows-1][j].isnumeric():
                    continue
                else:
                    right_end = j
                    break
            number = int(''.join(matrix[rows-1, left_start:right_end].tolist()))
            sum += number
            
            # Continue checking after the place of the last digit of the number
            i = right_end
            
    # Check the rest of the rows
    for row in range(1, rows-1):
        for i in range(cols):
            isPartNumber = True
            if not matrix[row][i].isnumeric():
                continue
            elif matrix[row][i].isnumeric():
                # char is a number, check left, right, up, down, and diagonals
                checked_places = [matrix[row][i-1], matrix[row][i+1], matrix[row-1][i], matrix[row+1][i], matrix[row-1][i+1], matrix[row-1][i-1], matrix[row+1][i+1], matrix[row+1][i-1]]
                if all(place in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] for place in checked_places):
                    isPartNumber = False
            if isPartNumber:
                print (matrix[0][i] + " is a number")
                # Get full number substring, i.e. check to the left and right and get all digits
                left_start = -1
                for j in range(i-1, -1, -1):
                    if matrix[row][j].isnumeric() and j == 0:
                        left_start = 0
                        break
                    if matrix[row][j].isnumeric():
                        continue
                    else: 
                        left_start = j+1
                        break
                right_end = -1
                for j in range(i+1, cols):
                    if matrix[row][j].isnumeric() and j == cols-1:
                        right_end = cols-1
                    if matrix[row][j].isnumeric():
                        continue
                    else:
                        right_end = j
                        break
                number = int(''.join(matrix[row, left_start:right_end].tolist()))
                sum += number
                
                # Continue checking after the place of the last digit of the number
                i = right_end
    print(sum)  
        
                
                    
            
    
part1()