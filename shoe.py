from deck import *

class Shoe:
    def __init__(self, num_decks=4):
        if num_decks < 1 or num_decks > 10:
            raise ValueError("Number of decks must be between 1 and 10.")
        
        self._num_decks = num_decks
        self._shoe = []

        for _ in range(self._num_decks):
            deck = Deck()
            for card in deck._deck:
                self._shoe.append(card)
        random.shuffle(self._shoe)

    def __str__(self):
        return ', '.join(str(card) for card in self._shoe)

shoe = Shoe(5)
print(len(shoe))