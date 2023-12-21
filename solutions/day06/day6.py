import math
lines = open('solutions/day6/input.txt').read().splitlines()
time_line = lines[0].split()
distance_line = lines[1].split()
times = [int(time_line[num]) for num in range(1, len(time_line))]
distances = [int(distance_line[num]) for num in range(1, len(distance_line))]

def part1():
    product = 1
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        
        # Quadratic formula to solve for x in equation -x^2 + times*x - distance = 0
        discriminant = time**2 - 4 * distance
        x1 = (-time + math.sqrt(discriminant)) / -2
        x2 = (-time - math.sqrt(discriminant)) / -2

        # Perturb to account for integer roots (breaks the number_solutions formula below)
        epsilon = 1e-6
        x1 += epsilon
        x2 -= epsilon
        number_solutions = math.floor(x2) - math.ceil(x1) + 1
        product *= number_solutions
        
    print(product)
    
def part2():
    # Join lists into ints
    time = int("".join(map(str, times)))
    distance = int("".join(map(str, distances)))
    product = 1
    # Quadratic formula to solve for x in equation -x^2 + times*x - distance = 0
    discriminant = time**2 - 4 * distance
    x1 = (-time + math.sqrt(discriminant)) / -2
    x2 = (-time - math.sqrt(discriminant)) / -2

    # Perturb to account for integer roots (breaks the number_solutions formula below)
    epsilon = 1e-6
    x1 += epsilon
    x2 -= epsilon
    number_solutions = math.floor(x2) - math.ceil(x1) + 1
    product *= number_solutions
        
    print(product)
    
part1()
part2()
        