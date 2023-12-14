lines = [line.strip().replace(" ", "") for line in open('solutions/day8/input.txt') if line.strip()]
directions = lines[0]
lines.pop(0)


location_map = {line.split("=")[0] : line.split("=")[1] for line in lines}
print(location_map)

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
    print(location, current_direction, count)
    current_direction = directions[count % len(directions)]
print(count)
    
    