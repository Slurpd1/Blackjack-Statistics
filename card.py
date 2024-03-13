class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return str(self._rank)+ str(self._suit)


# example card usage
# card = Card(2,'H')
# print(card)