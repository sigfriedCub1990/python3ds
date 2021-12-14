from unittest import TestCase
from stack import Stack

# Research about setup & teardown
class StackTests(TestCase):
    def test_should_return_empty(self):
        stack = Stack()

        actual = stack.is_empty()

        self.assertTrue(actual)

    def test_should_return_size(self):
        stack = Stack()

        expected = 0
        actual = stack.size()

        self.assertEqual(actual, expected)

    def test_should_add_new_item(self):
        stack = Stack()

        stack.push(1)

        expected = 1
        actual = stack.size()

        self.assertEqual(actual, expected)

    def test_should_pop_an_item(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)

        expected = 2
        actual = stack.pop()

        self.assertEqual(actual, expected)
        self.assertEqual(stack.size(), 1)

    def test_should_get_top_and_not_modify_stack(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)

        expected = 2
        actual = stack.peek()

        self.assertEqual(actual, expected)
        self.assertEqual(stack.size(), 2)
    def test_should_throw_if_trying_to_peek_from_empty_stack(self):
        stack = Stack()

        with self.assertRaises(RuntimeError) as cm:
            stack.peek()

        expected = 'Can not peek from an empty Stack'
        actual = str(cm.exception)

        self.assertEqual(actual, expected)
