from shoe import Shoe
from card import Card
from hand import Hand

def play_blackjack():
    # There is a dealer, player, and shoe
    dealer = Hand()
    player = Hand()
    shoe = Shoe(4)  # Playing with 4 decks
    shoe.shuffle()

    while True:
        # Playing a basic blackjack game with dealer
        player.add_card(shoe.deal_card())
        player.add_card(shoe.deal_card())

        dealer.add_card(shoe.deal_card())
        dealer.add_card(shoe.deal_card())

        dealer_upcard = dealer.show_upcard()
        print("Dealer's upcard:", dealer.show_upcard())  # Display only the first card (upcard)

        decision = input(f'Dealer has {dealer_upcard}. Your hand totals to {player.total_value()}, Would you like to hit or stand? (H,S)')

        if decision == 'H':
            # need to pull a card from the shoe
            dealt_card = shoe.deal_card()
            player.add_card(dealt_card)
            decision = input(f'Dealer has {dealer_upcard}. Your hand totals to {player.total_value()}, Would you like to hit or stand? (H,S)')


if __name__ == "__main__":
    play_blackjack()
