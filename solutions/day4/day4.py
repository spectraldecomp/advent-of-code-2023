lines = open('solutions/day4/input.txt').read().splitlines()


def day1():
    sum = 0
    for line in lines:
        card = line.split(':')
        print(card[0])
        num_pair= card[1].split('|')
        winning_numbers = num_pair[0].split()
        numbers = num_pair[1].split()
        print("Winning numbers: " + str(winning_numbers))
        print("Numbers: " + str(numbers))
        score = 0
        for number in numbers:
            if number in winning_numbers and score == 0:
                score = 1
            elif number in winning_numbers:
                score *= 2
        sum += score
        print("Score: " + str(score))
    print(sum)
    
def day2():
    copies = {}
    for i in range(len(lines)):
        card = lines[i].split(':')
        num_pair= card[1].split('|')
        winning_numbers = num_pair[0].split()
        numbers = num_pair[1].split()
        
        # Get number of matching numbers
        num_matches = 0
        for number in numbers:
            if number in winning_numbers:
                num_matches += 1

        # Add initial copy to copies
        if copies.get(i) is None:
            copies[i] = 1
        else: 
            copies[i] += 1
        
        for _ in range(copies[i]):
            # Add copies for each matching number
            for j in range(1, num_matches+1):
                if copies.get(i+j) is None:
                    copies[i+j] = 1
                else:
                    copies[i+j] += 1       
    print(sum(copies.values()))
day2()