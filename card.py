import unittest

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return str(self._rank)+ str(self._suit)
    
    def show_rank(self):
        return str(self._rank)
    
    def show_suit(self):
        return str(self._suit)
    
class testCard(unittest.TestCase):

    def


# example card usage
# card = Card(2,'H')
# print(card)