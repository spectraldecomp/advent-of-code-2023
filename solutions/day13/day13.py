import numpy as np

def load_data():
    with open('solutions/day13/input.txt') as f:
        data = f.read()
        raw_grids = data.split('\n\n')
        grids = []
        for raw_grid in raw_grids:
            grid = np.array([list(line) for line in raw_grid.split('\n')])
            grids.append(grid)
    return grids


def find_line_symmetry(grid, orientation):
    length = np.shape(grid)[1]
    for i in range(length):
        errors = 0
        is_line = True
        for j in range(length):
            if i+j+1 >= length:
                break
            if i-j < 0:
                break
            for k in range(np.shape(grid)[0]):
                if grid[k][i+j+1] != grid[k][i-j]:
                    if part == 1:
                        is_line = False
                    else:
                        errors += 1
        if part == 2 and errors == 1:
            if orientation == 'vertical':
                return i+1 if i != length-1 else -1
            if orientation == 'horizontal':
                return 100*(i+1) if i != length-1 else -1
        if part == 1 and is_line:
            if orientation == 'vertical':
                return i+1 if i != length-1 else -1
            if orientation == 'horizontal':
                return 100*(i+1) if i != length-1 else -1
    return -1
    
part = 2     
sum = 0
for grid in load_data():
    num1 = find_line_symmetry(grid, 'vertical')
    num2 = find_line_symmetry(grid.transpose(), 'horizontal')
    sum += num1 if num1 != -1 else num2
print(sum)
    
        
                
        
        