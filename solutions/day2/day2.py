import re
lines = open('solutions/day2/input.txt').read().splitlines()

def part1():
    sum = 0
    for line in lines:
        validLine = True
        gameId = line[:line.find(':')]
        line = line[line.find(':')+1:]
        line = line.replace(' ', '')
        games = line.split(';')
        for game in games:
            game = game.split(',')
            colorCount = {"red": 0, "green": 0, "blue": 0}
            for entry in game:
                count = int(re.findall('\d+', entry)[0])
                if 'red' in entry:
                    colorCount['red'] += count
                elif 'green' in entry:
                    colorCount['green'] += count
                elif 'blue' in entry:
                    colorCount['blue'] += count
                if colorCount['red'] > 12 or colorCount['green'] > 13 or colorCount['blue'] > 14:
                    validLine = False
        if validLine:
            sum += int(int(re.findall('\d+', gameId)[0]))
    print(sum)
    
def part2():
    sum = 0
    for line in lines:
        line = line[line.find(':')+1:]
        line = line.replace(' ', '')
        games = line.split(';')
        colorCount = {"red": 0, "green": 0, "blue": 0}
        for game in games:
            game = game.split(',')
            for entry in game:
                count = int(re.findall('\d+', entry)[0])
                if 'red' in entry:
                    colorCount['red'] = max(colorCount['red'], count)
                elif 'green' in entry:
                    colorCount['green'] = max(colorCount['green'], count)
                elif 'blue' in entry:
                    colorCount['blue'] = max(colorCount['blue'], count)
        power = colorCount['red'] * colorCount['green'] * colorCount['blue']
        sum+=power
    print(sum)
    
part1()    
part2()