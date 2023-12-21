import numpy as np



def expand_galaxy():
    lines = open('solutions/day11/input.txt').read().splitlines()
    g1 = np.array([list(line) for line in lines])
    rows = g1.shape[0]
    g2 = []
    for row in range(rows):
        if all(g1[row] == '.'):
            g2.append(g1[row])
            g2.append(g1[row])
        else:
            g2.append(g1[row])
    g2 = np.array(g2).transpose()
    g3 = []
    for row in range(rows):
        if all(g2[row] == '.'):
            g3.append(g2[row])
            g3.append(g2[row])
        else:
            g3.append(g2[row])   
    g3 = np.array(g3).transpose()
    return g3

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


galaxy = expand_galaxy()

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
        distance = manhattan_distance(x1, y1, x2, y2)
        sum += distance
    stars.remove(star1)

print(sum)
