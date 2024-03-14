import unittest
from card import Card
from hand import Hand

class TestHand(unittest.TestCase):

    def test_add_card(self):
        hand = Hand()
        card = Card('A', 'H')
        hand.add_card(card)
        self.assertEqual(hand.display_hand(), ['AH'])

    def test_total_value_with_11_aces(self):
        # Create a hand with 11 Aces
        hand = Hand([Card('A', 'H')] * 11)

        # The total value should be 21
        self.assertEqual(hand.total_value(), 21)
    
    def test_remove_card(self):
        hand = Hand([Card('A', 'H'), Card('K', 'S')])
        hand.remove_card(Card('A', 'H'))
        self.assertEqual(hand.display_hand(), ['KS'])

    def test_show_upcard(self):
        hand = Hand([Card('A', 'H'), Card('K', 'S')])
        self.assertEqual(hand.show_upcard(), 'A')

    def test_total_value(self):
        hand = Hand([Card('A', 'H'), Card('K', 'S')])
        self.assertEqual(hand.total_value(), 21)

    def test_is_bust(self):
        hand1 = Hand([Card('A', 'H'), Card('K', 'S')])
        hand2 = Hand([Card('K', 'S'), Card('Q', 'H'), Card('9', 'C')])

        self.assertFalse(hand1.is_bust())
        self.assertTrue(hand2.is_bust())

if __name__ == '__main__':
    unittest.main()
