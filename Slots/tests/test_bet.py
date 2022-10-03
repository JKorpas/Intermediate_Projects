from project.bet import Bet
import unittest


class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting class...")
        cls.bet_test = Bet()

    def test_where_bet_is_not_defined(self):
        self.assertEqual(self.bet_test.show_bet(), 1)


class TestClass2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting class...")
        cls.bet_test = Bet(5)

    def test_where_bet_is_equal_five(self):
        self.assertEqual(self.bet_test.show_bet(), 5)
