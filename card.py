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

    def __eq__(self, other):
        # two cards are equal if they have the same value
        return self._rank == other.show_rank()
    
    def __ne__(self, other):
        # two cards are equal if they have the same value
        return self._rank != other.show_rank()
    
    def __lt__(self, other):
        return self.valid_ranks.index(self._rank) < self.valid_ranks.index(other._rank)
    
    def __gt__(self,other):
        return self.valid_ranks.index(self._rank) > self.valid_ranks.index(other._rank)
    
    def __le__(self,other):
        return self.valid_ranks.index(self._rank) <= self.valid_ranks.index(other._rank)
    
    def __ge__(self,other):
        return self.valid_ranks.index(self._rank) >= self.valid_ranks.index(other._rank)
    
    def __add__(self,other):
        if self._rank in ['J','Q','K']:
            my_rank_value = 10
        elif self._rank is 'A':
            my_rank_value = 11
        else:
            my_rank_value = int(self._rank)
        
        if other._rank in ['J','Q','K']:
            other_rank_value = 10
        elif other._rank == 'A':
            other_rank_value = 11
        else:
            other_rank_value = int(other._rank)
        
        return  int(my_rank_value + other._rank)

# example card usage
# card = Card(2,'H')
# print(card)