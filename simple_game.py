from shoe import *
from card import *
from hand import *
from basic_strategy import *

def deal_initial_cards(player, dealer, shoe):
    """Deal initial cards to the player and dealer."""
    for _ in range(2):
        player.add_card(shoe.deal_card())
        dealer.add_card(shoe.deal_card())

def player_decision(player, dealer, shoe):
    """Handle player's decision-making."""
    decision = input(f"Dealer: {dealer.show_upcard()}\nYour hand: {', '.join(player.display_hand())}\nYour total: {player.total_value()}\nHit (H), Stand(S), or Double Down(D)? ")

    while decision.upper() == 'H' and player.total_value() < 21:
        dealt_card = shoe.deal_card()
        player.add_card(dealt_card)
        print(f'You drew: {dealt_card}')
        print(f'Your hand: {", ".join(player.display_hand())}, Total: {player.total_value()}')
        if player.total_value() == 21:
            break
        elif player.total_value() > 21:
            print("You bust!")
            break
        decision = input('Would you like to hit or stand? (H/S): ')

    if decision.upper() == 'D':
        dealt_card = shoe.deal_card()
        player.add_card(dealt_card)
        print(f'You doubled down and drew: {dealt_card}')
        print(f'Your hand: {", ".join(player.display_hand())}, Total: {player.total_value()}')

def dealer_play(dealer, shoe):
    """Handle dealer's turn."""
    while dealer.total_value() < 17:
        dealt_card = shoe.deal_card()
        dealer.add_card(dealt_card)
        if dealer.total_value() > 21:
            break

def determine_outcome(player, dealer, blackjack):
    """Determine the outcome of the game."""
    if blackjack:
        print(f'\nDealer has: {", ".join(dealer.display_hand())}, Total: {dealer.total_value()}\nYou have: {", ".join(player.display_hand())}, Total: {player.total_value()}\nBlackjack! You win!')
    elif player.total_value() > 21 or (dealer.total_value() > player.total_value()) or dealer.total_value() == 21:
        print(f'\nDealer has: {", ".join(dealer.display_hand())}, Total: {dealer.total_value()}\nYou have: {", ".join(player.display_hand())}, Total: {player.total_value()}\nYou lose!')
    elif player.total_value() == dealer.total_value():
        print(f'\nDealer has: {", ".join(dealer.display_hand())}, Total: {dealer.total_value()}\nYou have: {", ".join(player.display_hand())}, Total: {player.total_value()}\nPush!')
    else:
        print(f'\nDealer has: {", ".join(dealer.display_hand())}, Total: {dealer.total_value()}\nYou have: {", ".join(player.display_hand())}, Total: {player.total_value()}\nYou win!')

def play_blackjack():
    """Main function to play blackjack."""
    dealer = Hand()
    player = Hand()
    shoe = Shoe(4)  # Playing with 4 decks
    shoe.shuffle()

    while True:
        # Deal initial cards
        deal_initial_cards(player, dealer, shoe)

        # Check for blackjack
        blackjack = player.total_value() == 21

        if not blackjack:
            player_decision(player, dealer, shoe)

        # Player bust check
        if player.total_value() > 21:
            determine_outcome(player, dealer, blackjack)
            player.clear()
            dealer.clear()
            continue

        # Dealer's turn
        dealer_play(dealer, shoe)

        # Determine outcome
        determine_outcome(player, dealer, blackjack)
        print('\n')

        player.clear()
        dealer.clear()

if __name__ == "__main__":
    play_blackjack()
