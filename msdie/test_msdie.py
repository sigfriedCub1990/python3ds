import unittest
from msdie import MSDie

class MSDieTests(unittest.TestCase):
    def test_should_generate_random_number_in_range(self):
        instance = MSDie(6)

        actual = instance.roll()

        num_range = range(1, 7)
        result = actual in num_range

        self.assertTrue(result)

    def test_should_print_die_current_value(self):
        instance = MSDie(1)

        actual = str(instance)
        expected = "1"

        self.assertEqual(expected, actual)
