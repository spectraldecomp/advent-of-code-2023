import math
import functools
lines = [line.strip().replace(" ", "") for line in open('solutions/day8/input.txt') if line.strip()]
directions = lines[0]
lines.pop(0)


location_map = {line.split("=")[0] : line.split("=")[1] for line in lines}
starting_locations = [key for key in location_map.keys() if key[2] == 'A']
ending_locations = [key for key in location_map.keys() if key[2] == 'Z']
print(location_map)
print(starting_locations)
print(ending_locations)


def part1():
    location = 'AAA'
    current_direction = directions[0]
    count = 0

    while location != 'ZZZ':
        new_location = location_map[location]
        if current_direction == 'L':
            location = new_location[1:4]
        elif current_direction == 'R':
            location = new_location[5:8]
        count += 1
        current_direction = directions[count % len(directions)]
    print(count)
    
    
def part2():
    counts = []
    for location in starting_locations:
        current_direction = directions[0]
        count = 0
        while location not in ending_locations:
            new_location = location_map[location]
            if current_direction == 'L':
                location = new_location[1:4]
            elif current_direction == 'R':
                location = new_location[5:8]
            count += 1
            current_direction = directions[count % len(directions)]
        counts.append(count)
    # Get LCM of counts. math.lcm doesn't take list input so we use functools.reduce
    print(functools.reduce(math.lcm, counts))
        
        
print("Part 1:")
part1()
print("Part 2:")
part2()
    
    