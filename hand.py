from card import *
    
class Hand:
    def __init__(self, hand=None):
        if hand is None:
            hand = []  # Initialize an empty list if no hand is provided
        self._hand = hand

    # Other methods...

    def get_card_at_index(self, index):
        """
        Get the card object at the specified index in the hand.

        Args:
            index (int): The index of the card to retrieve.

        Returns:
            Card: The card object at the specified index.
        """
        if 0 <= index < len(self._hand):
            return self._hand[index]
        else:
            print("Index out of range.")
            return None
        
    def clear(self):
        self._hand = []

    def pop(self, index=-1):
        return self._hand.pop(index)

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
        self.hands = [Hand()]  # Initialize with a single empty hand
        self.num_of_splits = 0

    def execute_split(self, shoe, index=0):
        if not self.can_split():
            print("Cannot split again.")
            return

        # Add a new hand
        self.hands.append(Hand())

        # Move one card from the original hand to the new hand
        split_card = self.hands[index].pop()
        self.hands[index+1].add_card(split_card)

        # Deal an additional card to each hand from the shoe
        self.hands[index].add_card(shoe.deal_card())
        self.hands[index+1].add_card(shoe.deal_card())

        # Increment the number of splits made
        self.num_of_splits += 1



    def is_soft(self, index=0):
        # corrected to work with hand objects
        if self.hands[index].get_card_at_index(0).show_rank() == 'A' or self.hands[index].get_card_at_index(1).show_rank() == 'A':
            return True
        return False

    def can_split(self):
        return self.num_of_splits < 1 and self.hands[0].get_card_at_index(0).show_rank() == self.hands[0].get_card_at_index(1).show_rank()

    def add_card(self, card, hand_index=0):
        self.hands[hand_index].add_card(card)

    def clear(self):
        self.hands = [Hand()]
        

    def display_hand(self, index=0):
        return self.hands[index].display_hand()

    def total_value(self, index=0):
        return self.hands[index].total_value()

    def remove_card(self, card,index=0):
        self.hands[index].remove_card()

    def is_bust(self, hand_index=0):
        return self.total_value(hand_index) > 21
    
    def clear(self):
        self.hands = [Hand()]