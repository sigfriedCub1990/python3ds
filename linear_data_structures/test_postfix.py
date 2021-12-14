import unittest
from postfix import to_postfix_notation

class PostfixNotationTest(unittest.TestCase):


    def test_should_generate_postfix_notation(self):
        expression = "A + B * C"

        expected = ["A", "B", "C", "*", "+"]

        actual = to_postfix_notation(expression)

        self.assertEqual(actual, expected)


    def test_should_generate_postfix_with_parentheses(self):
        expression = "( A + B ) * C"

        expected = ["A", "B", "+", "C", "*"]

        actual = to_postfix_notation(expression)

        self.assertEqual(actual, expected)


    def test_should_generate_postfix_with_parentheses_2(self):
        expression = "( A + B ) * ( C + D )"

        expected = ["A", "B", "+", "C", "D", "+", "*"]

        actual = to_postfix_notation(expression)

        self.assertEqual(actual, expected)


    def test_should_generate_postfix_notation_2(self):
        expression = "A * B + C * D"

        expected = ["A", "B", "*", "C", "D", "*", "+"]

        actual = to_postfix_notation(expression)

        self.assertEqual(actual, expected)


    def test_should_generate_postfix_notation_3(self):
        expression = "A + B + C + D"

        expected = ["A", "B", "+", "C", "+", "D", "+"]

        actual = to_postfix_notation(expression)

        self.assertEqual(actual, expected)

    def test_should_generate_postfix_with_nested_parentheses(self):
        expression = "( A + ( B * ( C + D ) ) ) * E"

        expected = ["A", "B", "C", "D", "+", "*", "+", "E", "*"]

        actual = to_postfix_notation(expression)

        self.assertEqual(actual, expected)

    def test_should_generate_postfix_notation_4(self):
        expression = "( A + B ) * C - ( D - E ) * ( F + G )"
        expected = ["A", "B", "+", "C", "*", "D", "E", "-", "F", "G", "+","*", "-"]
        actual = to_postfix_notation(expression)

        self.assertEqual(actual, expected)


    def test_should_generate_postfix_with_exponent(self):
        expression = "A * B ^ ( C - D )"

        expected = ["A", "B", "C", "D", "-", "^", "*"]

        actual = to_postfix_notation(expression)

        self.assertEqual(actual, expected)
