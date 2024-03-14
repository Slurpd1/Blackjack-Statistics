from shoe import *
from card import *
from hand import *

# there is a dealer, player, and shoe

dealer = Hand()
player = Hand()
shoe = Shoe(4) # playing with 4 decks

player.add_card(shoe.deal_card()) # player has 2 cards
player.add_card(shoe.deal_card())

dealer.add_card(shoe.deal_card()) # dealer has 2 cards
dealer.add_card(shoe.deal_card())

upcard = dealer.show_upcard()  # Get the upcard
if upcard != "No cards in hand":  # Check if there is an upcard
    print(f"dealer has {upcard}")
else:
    print("Dealer has no upcard")

decision = input("Hit, stand, double down, or split?")
while decision not in ['H','S','D','SP']:
    decision = input("Hit, stand, double down, or split?")