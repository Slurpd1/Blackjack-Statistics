def basicStrategy(handType, playerHand, dealerTotal):
    # dh      2,   3,   4,   5,   6,   7,   8,   9   10,  A
    hard_basicStrategy = [
        ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], #4-8
        ['H', 'DH', 'DH', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'], #9
        ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H', 'H'], #10
        ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H'], #11
        ['H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], #12
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], #13 
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], #14
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], #15
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], #16
        ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], #17+ 
        ]   
# dh      2,   3,   4,   5,   6,   7,   8,   9   10,  A
    soft_basicStrategy = [
        ['H', 'H', 'H', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'], #13
        ['H', 'H', 'H', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'], #14
        ['H', 'H', 'DH', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'], #15
        ['H', 'H', 'DH', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'], #16
        ['H', 'DH', 'DH', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'], #17
        ['S', 'DS', 'DS', 'DS', 'DS', 'S', 'S', 'H', 'H', 'H'], #18
        ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], #19+
        ]   
    
# dh      2,   3,   4,   5,   6,   7,   8,   9   10,  A
    splits = [
        ['P', 'P', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H'], # 2,2
        ['P', 'P', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H'], # 3,3
        ['H', 'H', 'H', 'P', 'P', 'H', 'H', 'H', 'H', 'H'], # 4,4
        ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H', 'H'], # 5,5
        ['H', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H', 'H'], # 6,6
        ['P', 'P', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H'], # 7,7
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], # 8,8
        ['P', 'P', 'P', 'P', 'P', 'S', 'P', 'P', 'S', 'S'], # 9,9
        ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # 10,10
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], # A,A
        ]
    col = get_col(dealerTotal)
    row = get_row(handType, playerHand)

    if handType == 'hard':
        return hard_basicStrategy[row][col]
    elif handType == 'soft':
        return soft_basicStrategy[row][col]
    else:
        return splits[row][col]
        


def get_col(dealerTotal):
    if dealerTotal == '2':
        col = 0
    elif dealerTotal == '3':
        col = 1
    elif dealerTotal == '4':
        col = 2
    elif dealerTotal == '5':
        col = 3
    elif dealerTotal == '6':
        col = 4
    elif dealerTotal == '7':
        col = 5
    elif dealerTotal == '8':
        col = 6
    elif dealerTotal == '9':
        col = 7
    elif dealerTotal == '10' or dealerTotal == 'J' or dealerTotal == 'Q' or dealerTotal == 'K':
        col = 8
    elif dealerTotal == 'A':
        col = 9
    return col

def get_row(handType, playerHand):
    if handType == 'soft':
        # there is a very rare case here where we get an ace and an ace which can no longer be split
        # since game is being played with one split allowed. so technically we can have a soft 12
        if playerHand.total_value() == 12:
            row = 0
        if playerHand.total_value() == 13:
            row = 0
        if playerHand.total_value() == 14:
            row = 1
        if playerHand.total_value() == 15:
            row = 2
        if playerHand.total_value() == 16:
            row = 3
        if playerHand.total_value() == 17:
            row = 4
        if playerHand.total_value() == 18:
            row = 5
        if playerHand.total_value() >= 19:
            row = 6
    elif handType == 'hard':
        if playerHand.total_value() <= 8:
            row = 0
        if playerHand.total_value() == 9:
            row = 1
        if playerHand.total_value() == 10:
            row = 2
        if playerHand.total_value() == 11:
            row = 3
        if playerHand.total_value() == 12:
            row = 4
        if playerHand.total_value() == 13:
            row = 5
        if playerHand.total_value() == 14:
            row = 6
        if playerHand.total_value() == 15:
            row = 7
        if playerHand.total_value() == 16:
            row = 8
        if playerHand.total_value() >= 17:
            row = 9
    elif handType == 'split':
        try:
            split_rank = playerHand.hands[0].get_card_at_index(0).show_rank()
        except AttributeError:
            split_rank = playerHand._hand[0].show_rank()

        if split_rank == '2':
            row = 0
        if split_rank == '3':
            row = 1
        if split_rank == '4':
            row = 2
        if split_rank == '5':
            row = 3
        if split_rank == '6':
            row = 4
        if split_rank == '7':
            row = 5
        if split_rank == '8':
            row = 6
        if split_rank == '9':
            row = 7
        if split_rank == '10' or split_rank == 'J' or split_rank == 'Q' or split_rank == 'K':
            row = 8
        if split_rank == 'A':
            row = 9
    return row

