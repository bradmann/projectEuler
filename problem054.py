'''
Created on Nov 9, 2011

@author: bradmann
'''

def toscalar(card):
    if type(card) == str:
        val = card[0]
        if val == 'T': return 10
        if val == 'J': return 11
        if val == 'Q': return 12
        if val == 'K': return 13
        if val == 'A': return 14
        return int(val)
    if type(card) == list:
        return [toscalar(c) for c in card]  

def is_royal_flush(hand):
    vals = set([card[0] for card in hand])
    if is_flush(hand) and 'T' in vals and 'J' in vals and 'Q' in vals and 'K' in vals and 'A' in vals:
        return True
    return False

def is_straight_flush(hand):
    if is_straight(hand) and is_flush(hand):
        return True
    return False
    
def is_4_of_a_kind(hand):
    vals = toscalar(hand)
    for val in vals:
        if vals.count(val) >= 4:
            return True
    return False
    
def is_full_house(hand):
    vals = set([card[0] for card in hand])
    count = [card[0] for card in hand].count(hand[0][0])
    if len(vals) == 2 and count < 4:
        return True
    return False

def is_flush(hand):
    suits = set([card[1] for card in hand])
    return len(suits) == 1

def is_straight(hand):
    vals = sorted(toscalar(hand))
    if vals[0] + 4 == vals[1] + 3 == vals[2] + 2 == vals[3] + 1 == vals[4]:
        return True
    return False

def is_3_of_a_kind(hand):
    vals = toscalar(hand)
    for val in vals:
        if vals.count(val) == 3:
            return True
    return False

def is_2_pair(hand):
    vals = toscalar(hand)
    totals = {}
    for val in vals:
        count = totals.setdefault(val, 0)
        totals[val] = count + 1
    pairs = 0
    for v in totals.values():
        if v >= 2:
            pairs += 1
    if pairs > 1:
        return True
    else:
        return False
    
def is_pair(hand):
    vals = set(toscalar(hand))
    return len(vals) < 5

def pair_value(hand):
    vals = toscalar(hand)
    freqs = {}
    value = 0
    for val in vals:
        freqs[val] = freqs.setdefault(val, 0) + 1
    for key in freqs.keys():
        if freqs[key] == 2:
            value += key*2
    return value

def three_of_a_kind_value(hand):
    vals = toscalar(hand)
    freqs = {}
    value = 0
    for val in vals:
        freqs[val] = freqs.setdefault(val, 0) + 1
    for key in freqs.keys():
        if freqs[key] == 3:
            value += key*3
    return value
        

def high_card(hand):
    return max(toscalar(hand))
    

def rank(hand):
    if (is_royal_flush(hand)):
        return 23
    elif(is_straight_flush(hand)):
        return 22
    elif(is_4_of_a_kind(hand)):
        return 21
    elif(is_full_house(hand)):
        return 20
    elif(is_flush(hand)):
        return 19
    elif(is_straight(hand)):
        return 18
    elif(is_3_of_a_kind(hand)):
        return 17
    elif(is_2_pair(hand)):
        return 16
    elif(is_pair(hand)):
        return 15
    else:
        return sorted(toscalar(hand))[-1]
    
def tie_break(hand1, hand2, rank):
    if rank == 15 or rank == 16:
        v1 = pair_value(hand1)
        v2 = pair_value(hand2)
        return v1 > v2
    if rank == 17:
        v1 = three_of_a_kind_value(hand1)
        v2 = three_of_a_kind_value(hand2)
        return v1 > v2
    if rank == 18 or rank == 19:
        v1 = high_card(hand1)
        v2 = high_card(hand2)
        return v1 > v2
        
    return False

if __name__ == '__main__':
    f = open('data/poker.txt', 'r')
    wins1 = 0
    wins2 = 0
    ties = 0
    for line in f.readlines():
        cards = line.strip().split(' ')
        hand1 = cards[:5]
        hand2 = cards[5:]
        
        rank1 = rank(hand1)
        rank2 = rank(hand2)
        print("hand1: " + " ".join(hand1) + " Rank: " + str(rank1))
        print("hand2: " + " ".join(hand2) + " Rank: " + str(rank2))
        if rank1 > rank2:
            wins1 += 1
        elif rank1 < rank2:
            wins2 += 1
        else:
            if tie_break(hand1, hand2, rank1):
                wins1 += 1
            else:
                wins2 += 1
    print(str(wins1) + ', ' + str(wins2))