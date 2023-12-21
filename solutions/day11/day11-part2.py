import numpy as np

lines = open('solutions/day11/input.txt').read().splitlines()
galaxy = np.array([list(line) for line in lines])

def calc_distance(x1, y1, x2, y2):
    distance = 0
    # Check each point between x1 and x2
    abs_x = abs(x1 - x2)
    abs_y = abs(y1 - y2)
    for point in range(abs_x):
        if x1 < x2:
            
            if all(galaxy[x1+point][y] == '.' for y in range(0, galaxy.shape[1])):
                distance += 1e6
            else:
                distance += 1
        else:
            if all(galaxy[x1-point][y] == '.' for y in range(0, galaxy.shape[1])):
                distance += 1e6
            else:
                distance += 1
                
    # Check each point between y1 and y2
    for point in range(abs_y):
        if y1 < y2:
            if all(galaxy[x][y1+point] == '.' for x in range(0, galaxy.shape[0])):
                distance += 1e6
            else:
                distance += 1
        else:
            if all(galaxy[x][y1-point] == '.' for x in range(0, galaxy.shape[0])):
                distance += 1e6
            else:
                distance += 1
                
    return distance



num_stars = sum(sum(galaxy == '#'))
stars = [num for num in range(0, num_stars)]
coords = np.where(galaxy == '#')
print(coords)
sum = 0
count = 0
# We go backwards because removing elts from the list while iterating over it
# skips over some elts
for star1 in stars[::-1]:
    for star2 in stars:
        if star1 == star2:
            continue
        count += 1
        x1, y1 = coords[0][star1], coords[1][star1]
        x2, y2 = coords[0][star2], coords[1][star2]
        distance = calc_distance(x1, y1, x2, y2)
        sum += distance
    stars.remove(star1)


print(sum)
