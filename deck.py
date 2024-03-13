from card import *
import random

class Deck:
    def __init__(self):
        self._deck = []
        for rank in ['A','2','3','4','5','6','7','8','9','J','Q','K']:
            for suit in ['C','D','H','S']:
                card = Card(rank, suit)
                self._deck.append(card)

    def __str__(self):
        return ', '.join(str(card) for card in self._deck)
    
    def shuffle_deck(self):
        random.shuffle(self._deck)
    
# deck = Deck()
# deck.shuffle_deck()
# print(deck)

