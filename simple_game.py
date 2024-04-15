from shoe import *
from card import *
from hand import *
from basic_strategy import *

# there is a dealer, player, and shoe

def game():
    dealer = Hand()
    player = Hand()
    shoe = Shoe(4) # playing with 4 decks
    shoe.shuffle()


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

    basic_strategy = BasicStrategy()

    # this is where the function will come in that decides what to play

    # while decision != stand:
    #   pass total and dealer uphand to function
    #   total must have an H or S in front of it
    


if __name__ == "__main__":
    game()