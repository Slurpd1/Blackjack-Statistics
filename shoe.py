from deck import *
from card import *

class Shoe:
    # a shoe is just multuple decks.

    def __init__(self, num_decks=4):
        self._shoe = []
        self._num_decks = num_decks

        for i in range(self._num_decks):
            for rank in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
                for suit in ['C','D','H','S']:
                    card = Card(rank, suit)
                    self._shoe.append(card)

    def __str__(self):
        return ', '.join(str(card) for card in self._shoe)

    def shuffle(self):
        random.shuffle(self._shoe)

    def deal_card(self):
        card = self._shoe.pop()
        return card
    
    def num_decks(self):
        return self._num_decks
    
    def amount_left(self):
        total_cards = self._num_decks * 52
        remaining_cards = len(self._shoe)
        return (remaining_cards / total_cards) * 100



