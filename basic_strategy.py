class BasicStrategy:
    def __init__(self, my_hand, dealer_upcard):
        self._my_hand_total = my_hand
        self._dealer_upcard = dealer_upcard

    def is_my_total_soft(self):
        self._my_hand_total

    def is_dealer_upcard_ace(self):
        if self.dealer_upcard.show_card() == 'A':
            return True
        return False   

    def basic_strategy(self):
        # if hand is hard total (i.e. no ace)
        pass