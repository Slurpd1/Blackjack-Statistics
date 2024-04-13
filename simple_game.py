from shoe import *
from card import *
from hand import *

# there is a dealer, player, and shoe
dealer = Hand()
player = Hand()
shoe = Shoe(4) # playing with 4 decks
shoe.shuffle()

while True:
    # playing a basic blackjack game with dealer
    player.add_card(shoe.deal_card())
    player.add_card(shoe.deal_card())

    dealer.add_card(shoe.deal_card())
    dealer.add_card(shoe.deal_card())
    
    print("dealer hand")
    print(dealer.display_hand())
    print(dealer.show_upcard())

    print("player hand")
    print(player.display_hand())
    print(player.total_value())

if __name__ == "__main__":
    game()