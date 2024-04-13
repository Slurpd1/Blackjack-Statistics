class BasicStrategy:
    def __init__(self, my_hand, dealer_upcard):
        self._my_hand_total = my_hand
        self._dealer_upcard = dealer_upcard

    def is_my_total_soft(self):
        pass