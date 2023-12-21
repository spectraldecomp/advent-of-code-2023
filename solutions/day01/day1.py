input_lines = open('solutions/day1/input.txt').read().splitlines()
sum = 0
for line in input_lines:
    num = []
    keywords = {'one': 'one1one', 'two': 'two2two', 'three': 'three3three', 'four': 'four4four', 'five': 'five5five', 'six': 'six6six', 'seven': 'seven7seven', 'eight': 'eight8eight', 'nine': 'nine9nine'}

    # replace all occurences of keywords with their corresponding values
    for key in keywords:
        line = line.replace(key, keywords[key])
                        
    # check from the left
    for i in range(len(line)):
        if line[i].isdigit():
            num.append(line[i])
            break
    
    # check from the right
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            num.append(line[i])
            break
    # convert list to string
    num = ''.join(num)
    sum += int(num)
print(sum)
    