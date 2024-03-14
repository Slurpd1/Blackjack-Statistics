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

    def test_cards_equality(self):
        card1 = Card('A', 'H')
        card2 = Card('A', 'S')
        card3 = Card('K', 'S')

        self.assertEqual(card1, card2)
        self.assertNotEqual(card1, card3)

    def test_equal(self):
        card1 = Card('A', 'H')
        card2 = Card('A', 'H')
        card3 = Card('K', 'S')

        self.assertEqual(card1, card2)
        self.assertNotEqual(card1, card3)

    def test_not_equal(self):
        card1 = Card('A', 'H')
        card2 = Card('A', 'H')
        card3 = Card('K', 'S')

        self.assertFalse(card1 != card2)
        self.assertTrue(card1 != card3)

    def test_less_than(self):
        card1 = Card('2', 'H')
        card2 = Card('K', 'S')

        self.assertTrue(card1 < card2)
        self.assertFalse(card2 < card1)

    def test_greater_than(self):
        card1 = Card('K', 'S')
        card2 = Card('2', 'H')

        self.assertTrue(card1 > card2)
        self.assertFalse(card2 > card1)

    def test_less_than_or_equal(self):
        card1 = Card('2', 'H')
        card2 = Card('K', 'S')
        card3 = Card('2', 'H')

        self.assertTrue(card1 <= card2)
        self.assertFalse(card2 <= card1)
        self.assertTrue(card1 <= card3)

    def test_greater_than_or_equal(self):
        card1 = Card('K', 'S')
        card2 = Card('2', 'H')
        card3 = Card('K', 'S')

        self.assertTrue(card1 >= card2)
        self.assertFalse(card2 >= card1)
        self.assertTrue(card1 >= card3)

    

if __name__ == '__main__':
    unittest.main()