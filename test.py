import unittest
from card import Card

class TestCard(unittest.TestCase):

    def test_card_creation(self):
        card = Card('A', 'S')
        self.assertEqual(card.show_rank(), 'A')
        self.assertEqual(card.show_suit(), 'S')

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            card = Card('101', 'Diamonds')
        with self.assertRaises(ValueError):
            card = Card('2', 'Z')
            
    def test_str(self):
        card = Card('A','S')
        self.assertEqual(card.__str__(), 'AS')

        card = Card('10','H')
        self.assertEqual(card.__str__(), '10H')

if __name__ == '__main__':
    unittest.main()