from project.deposit import Deposit
import unittest


class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting class...")
        cls.deposit_test = Deposit(5)

    def test_where_deposit_equals_five(self):
        self.assertEqual(self.deposit_test.show_deposit(), 5)
