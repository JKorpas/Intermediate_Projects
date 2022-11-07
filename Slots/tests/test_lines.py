from project.lines import Lines
import unittest


class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting class...")
        cls.lines_test = Lines(3)

    def test_where_lines_equals_three(self):
        self.assertEqual(self.lines_test.show_lines(), 3)
