import unittest
from deque import Deque

class DequeTests(unittest.TestCase):
    def test_should_add_front_item(self):
        deque = Deque()

        deque.add_front(1)
        deque.add_front(2)

        expected = 2
        actual = deque.remove_front()

        self.assertEqual(actual, expected)

    def test_shoud_add_rear_item(self):
        deque = Deque()

        deque.add_rear(2)
        deque.add_rear(1)

        expected = 1
        actual = deque.remove_rear()

        self.assertEqual(actual, expected)
