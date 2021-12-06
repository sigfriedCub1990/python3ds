
import unittest
from fraction import Fraction

# TODO: Re-implement all tests
class FractionTests(unittest.TestCase):
    def test_should_add_fractions(self):
        first = Fraction(1, 2)
        second = Fraction(1, 3)

        expected = '5/6'
        actual = str(first + second)

        self.assertEqual(actual, expected)
