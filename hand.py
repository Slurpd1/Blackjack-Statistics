class Hand:
    def __init__(self, hand=None):
        if hand is None:
            hand = []  # Initialize an empty list if no hand is provided
        self._hand = hand

    def clear(self):
        self._hand = []

    def dealer_turn(self, card):
        while self.total_value() < 17:
            self.add_card(card)
            if self.total_value() > 21:
                return
        return
    
    def add_card(self, card):
        self._hand.append(card)

    def show_upcard(self):
        if self._hand:  # Check if hand is not empty
            return str(self._hand[0].show_rank())
        else:
            return "No cards in hand"
        
    def display_hand(self):
        return [str(card) for card in self._hand]
    
    def total_value(self):
        total = 0
        ace_count = 0
        for card in self._hand:
            if card.show_rank() in {'J', 'Q', 'K'}:
                total += 10
            elif card.show_rank() == 'A':
                total += 11
                ace_count += 1
            else:
                total += int(card.show_rank())

            # Adjust Ace value to 1 if bust
        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1
        
        return total
    
    def remove_card(self, card):
        if card in self._hand:
            self._hand.remove(card)
        else:
            print("Card not found in hand")
    
    def is_bust(self):
        return self.total_value() > 21
    

class PlayerHand:
    def __init__(self):
        self.hands = [[]]  # Initialize with a single empty hand

    def execute_split(self, shoe, index):
        if not self.can_split():
            return TypeError
        self.hands.append([])
        original_hand = self.hands[index]
        split_card = original_hand.pop()
        original_hand.append(shoe.deal_card())
        self.hands[index+1].extend([split_card, shoe.deal_card()])



    def is_soft(self, index=0):
        hand = self.hands[index]
        card1 = hand[0]
        card2 = hand[1]
        if card1.show_rank().upper() == 'A' or card2.show_rank().upper() == 'A':
            return True
        return False

    def can_split(self):
        for hand in self.hands:
            if (hand[0] == hand[1]) and (len(hand) == 2):
                return True
        return False

    def add_card(self, card, hand_index=0):
        self.hands[hand_index].append(card)

    def clear(self):
        self._hand = []
        

    def display_hand(self, hand_index=0):
        return [str(card) for card in self.hands[hand_index]]

    def total_value(self, hand_index=0):
        total = 0
        ace_count = 0
        for card in self.hands[hand_index]:
            if card.show_rank() in {'J', 'Q', 'K'}:
                total += 10
            elif card.show_rank() == 'A':
                total += 11
                ace_count += 1
            else:
                total += int(card.show_rank())

        # Adjust Ace value to 1 if bust
        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1

        return total

    def remove_card(self, card, hand_index=0):
        if card in self.hands[hand_index]:
            self.hands[hand_index].remove(card)
        else:
            print("Card not found in hand")

    def is_bust(self, hand_index=0):
        return self.total_value(hand_index) > 21
    
    def clear(self):
        self.hands = [[]]


