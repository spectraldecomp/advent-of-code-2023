lines = open('solutions/day7/input.txt').read().splitlines()


    

def get_hand_type(hand):
    card_map = {}
    for card in hand:
        if card in card_map:
            card_map[card] += 1
        else:
            card_map[card] = 1
    jokers = 0        
    # Add jokers
    if 'J' in card_map:
        jokers = card_map['J']
        del card_map['J']
        
    '''THIS IS DISGUSTING IM VERY SORRY BUT I JUST WANNA GO TO THE NEXT DAY MAN'''
    # Check for 5-of-a-kind
    if (5 in card_map.values()) or (jokers == 5) or (4 in card_map.values() and jokers == 1) or (3 in card_map.values() and jokers == 2) or (2 in card_map.values() and jokers == 3) or (1 in card_map.values() and jokers == 4):
        return 6
    # Check for 4-of-a-kind
    if (4 in card_map.values()) or (3 in card_map.values() and jokers == 1) or (2 in card_map.values() and jokers == 2) or (1 in card_map.values() and jokers == 3):
        return 5
    # Check for full house
    if (3 in card_map.values() and 2 in card_map.values()) or (3 in card_map.values() and jokers == 1) or (list(card_map.values()).count(2) == 2 and jokers == 1):
        return 4
    # Check for 3-of-a-kind
    if (3 in card_map.values()) or (2 in card_map.values() and jokers == 1) or (1 in card_map.values() and jokers == 2):
        return 3
    # Check for 2-pair
    if list(card_map.values()).count(2) == 2:
        return 2
    # Check for pair
    if 2 in card_map.values() or jokers == 1:
        return 1
    # Check for high card
    return 0
    
    
    
def order_by_high_card(hands):
    order = 'AKQT98765432J'
    return sorted(hands, key=lambda x: [order.index(char) for char in x[0]], reverse=True)
   
# Construct bid map
bid_map = {}
for line in lines:
    hand, bid = line.split()
    bid = int(bid)
    
    hand_type = get_hand_type(hand)
    
    bid_map[hand] = (hand, get_hand_type(hand), bid)
    
# Order by bid
sorted_hands = sorted(bid_map.values(), key=lambda x: x[1], reverse=True)
sorted_hands_by_type = []
for i in range(7):
    sorted_hands_by_type.append([hand for hand in sorted_hands if hand[1] == i])
    
# Order by high card
for i in range(7):
    if sorted_hands_by_type[i]:
        sorted_hands_by_type[i] = order_by_high_card(sorted_hands_by_type[i])

rank = []
for i in range(7):
    for hand in sorted_hands_by_type[i]:
        rank.append(hand[2])
    
winnings = [rank[i] * (i + 1) for i in range(len(rank))]
print(sum(winnings))

    
    
    
    