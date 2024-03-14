class Hand:
    def __init__(self, hand=None):
        if hand is None:
            hand = []  # Initialize an empty list if no hand is provided
        self._hand = hand

    def add_card(self, card):
        self._hand.append(card)

    def show_upcard(self):
        print("Value of self._hand:", self._hand)
        if self._hand:  # Check if hand is not empty
            return str(self._hand[0].show_rank())
        else:
            return "No cards in hand"
