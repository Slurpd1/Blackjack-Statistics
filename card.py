import unittest

class Card:
    valid_ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    valid_suits = ['H','C','S','D']
    def __init__(self, rank, suit):
        
        if rank not in self.valid_ranks:
            raise ValueError("Invalid rank.")
        if suit not in self.valid_suits:
            raise ValueError("Invalid suit.")

        self._rank = rank
        self._suit = suit
        

    def __str__(self):
        return str(self._rank)+ str(self._suit)
    
    def show_rank(self):
        return str(self._rank)
    
    def show_suit(self):
        return str(self._suit)



# example card usage
# card = Card(2,'H')
# print(card)