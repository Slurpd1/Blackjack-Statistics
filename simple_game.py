from shoe import *
from card import *
from hand import *
from basic_strategy import *

def play_blackjack():
    # There is a dealer, player, and shoe
    dealer = Hand()
    player = Hand()
    shoe = Shoe(4)  # Playing with 4 decks
    shoe.shuffle()

    while True:
        blackjack = False
        # currently the shoe WILL EMPTY OUT. Check before playing
        # Playing a basic blackjack game with dealer
        player.add_card(shoe.deal_card())
        player.add_card(shoe.deal_card())

        dealer.add_card(shoe.deal_card())
        dealer.add_card(shoe.deal_card())

        dealer_upcard = dealer.show_upcard()

        if player.total_value() == 21:
            blackjack = True

        if not blackjack:
            decision = input(f"Dealer: {dealer_upcard}\nYour hand: {', '.join(player.display_hand())}\nYour total: {player.total_value()}\nHit (H), Stand(S), or Double Down(D)?")



        while player.total_value() < 21:
            if player.total_value() > 21:
                break
            if player.total_value == 21:
                break
            if decision.upper() == 'H':
                # need to pull a card from the shoe
                dealt_card = shoe.deal_card()
                player.add_card(dealt_card)
                if int(player.total_value()) == 21:
                    break
                if player.total_value() > 21:
                    break
                decision = input(f"\nDealer: {dealer_upcard}\nYour hand: {', '.join(player.display_hand())}\nYour total: {player.total_value()}\nHit (H), or Stand(S)?")
            if decision.upper() == 'D':
                dealt_card = shoe.deal_card()
                player.add_card(dealt_card)
                break
            if decision.upper() == 'S':
                break

        while dealer.total_value() < 17 and not blackjack:
            dealt_card = shoe.deal_card()
            dealer.add_card(dealt_card)
            if dealer.total_value() > 21:
                break 

        if dealer.total_value() > 21:
            print(f'\nDealer has {', '.join(dealer.display_hand())}\tTotal {dealer.total_value()}\nYou have {', '.join(player.display_hand())}\t  Total {player.total_value()}\n You win!')
            print('\n')
        elif (player.total_value() > 21 or (dealer.total_value() > player.total_value()) or dealer.total_value() == 21) and (not blackjack):
            print(f'\nDealer has {', '.join(dealer.display_hand())}\tTotal {dealer.total_value()}\nYou have {', '.join(player.display_hand())}\t  Total {player.total_value()}\n You lose!')
            print('\n')
        elif player.total_value() == dealer.total_value():
            print(f'\nDealer has {', '.join(dealer.display_hand())}\tTotal {dealer.total_value()}\nYou have {', '.join(player.display_hand())}\t  Total {player.total_value()}\n push')
            print('\n')
        elif blackjack:
            print(f'\nDealer has {', '.join(dealer.display_hand())}\tTotal {dealer.total_value()}\nYou have {', '.join(player.display_hand())}\t  Total {player.total_value()}\n Blackjack')
            print('\n')
        else:
            print(f'\nDealer has {', '.join(dealer.display_hand())}\tTotal {dealer.total_value()}\nYou have {', '.join(player.display_hand())}\t  Total {player.total_value()}\n You win!')
            print('\n')

        player.clear()
        dealer.clear()

if __name__ == "__main__":
    play_blackjack()
