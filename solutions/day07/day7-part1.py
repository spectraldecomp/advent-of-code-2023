lines = open('solutions/day7/input.txt').read().splitlines()


    

def get_hand_type(hand):
    card_map = {}
    for card in hand:
        if card in card_map:
            card_map[card] += 1
        else:
            card_map[card] = 1
            
    if 5 in card_map.values():
        return 6
    if 4 in card_map.values():
        return 5
    if 3 in card_map.values() and 2 in card_map.values():
        return 4
    if 3 in card_map.values():
        return 3
    if len(card_map) == 3:
        return 2
    if len(card_map) == 4:
        return 1
    else:
        return 0
    
def order_by_high_card(hands):
    order = 'AKQJT98765432'
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

    
    
    
    