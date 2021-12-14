#!/usr/bin/python
import unittest
from binary_converter import to_binary, base_converter

class BinaryConverterTests(unittest.TestCase):
    def test_should_convert_number_5(self):
        expected = "101"
        actual = to_binary(5)

        self.assertEqual(actual, expected)

    def test_should_convert_to_base_16(self):
        expected = '11'
        actual = base_converter(17, 16)

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
