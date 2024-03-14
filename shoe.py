from deck import *
from card import *

class Shoe:
    # a shoe is just multuple decks.

    def __init__(self, num_decks):
        self._shoe = []

        for i in range(num_decks):
            for rank in ['A','2','3','4','5','6','7','8','9','J','Q','K']:
                for suit in ['C','D','H','S']:
                    card = Card(rank, suit)
                    self._shoe.append(card)

    def __str__(self):
        return ', '.join(str(card) for card in self._shoe)

    def shuffle(self):
        random.shuffle(self._shoe)

    def deal_card(self):
        self._shoe.pop()