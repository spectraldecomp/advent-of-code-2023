lines = open('solutions/day15/input.txt').read().splitlines()

def HASH(s):
    current_val = 0
    for char in s:
        current_val += ord(char)
        current_val *= 17
        current_val = current_val % 256
    return current_val

map = {i: [] for i in range(256)}
for line in lines:
    steps = line.split(",")
    for step in steps:
        if '-' in step:
            label = step.split("-")[0]
            if HASH(label) in map:
                map[HASH(label)] = [item for item in map[HASH(label)] if item[0] != label]
        if '=' in step:
            label = step.split("=")[0]
            focal_length = int(step.split("=")[1])
            if HASH(label) in map:
                if label in [item[0] for item in map[HASH(label)]]:
                    index = [item[0] for item in map[HASH(label)]].index(label)
                    map[HASH(label)][index] = (label, focal_length)
                else:
                    map[HASH(label)].append((label, focal_length))
sum = 0                
for key in map:
    if map[key]:
        for i, item in enumerate(map[key]):
            sum += (key + 1) * item[1] * (i + 1)
print(sum)


