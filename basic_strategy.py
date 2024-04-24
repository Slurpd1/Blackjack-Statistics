def basicStrategy(handType, playerHand, dealerTotal):
    # dh      2,   3,   4,   5,   6,   7,   8,   9   10,  A
    hard_basicStrategy = [
        ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], #4-8
        ['H', 'DH', 'DH', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'], #9
        ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H', 'H'], #10
        ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H'], #11
        ['H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], #12
        ['s', 's', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], #13 
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
        ['PH', 'PH', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H'], # 2,2
        ['PH', 'PH', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H'], # 3,3
        ['H', 'H', 'H', 'PH', 'PH', 'H', 'H', 'H', 'H', 'H'], # 4,4
        ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H', 'H'], # 5,5
        ['PH', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H', 'H'], # 6,6
        ['P', 'P', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H'], # 7,7
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], # 8,8
        ['P', 'P', 'P', 'P', 'P', 'S', 'P', 'P', 'S', 'S'], # 9,9
        ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # 10,10
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], # A,A
        ]
    col = get_col(dealerTotal)
    row = get_row(handType, playerHand)

    if handType == 'hard':
        print('hard')
        return hard_basicStrategy[row][col]
    elif handType == 'soft':
        print('soft')
        return soft_basicStrategy[row][col]
    else:
        print('split')
        return splits[row][col]
        


def get_col(dealerTotal):
    col_map = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'A': 9}
    return col_map.get(str(dealerTotal), None)

def get_row(handType, playerHand):
    if handType == 'soft':
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
        if playerHand.hands[0][0].show_rank == '2':
            row = 0
        if playerHand.hands[0][0].show_rank == '3':
            row = 1
        if playerHand.hands[0][0].show_rank == '4':
            row = 2
        if playerHand.hands[0][0].show_rank == '5':
            row = 3
        if playerHand.hands[0][0].show_rank == '6':
            row = 4
        if playerHand.hands[0][0].show_rank == '7':
            row = 5
        if playerHand.hands[0][0].show_rank == '8':
            row = 6
        if playerHand.hands[0][0].show_rank == '9':
            row = 7
        if playerHand.hands[0][0].show_rank == '10':
            row = 8
        if playerHand.hands[0][0].show_rank == 'A':
            row = 9
    return row
    
    return row_maps.get(handType, {}).get(total_value, None)

