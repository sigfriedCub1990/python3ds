import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    def test_should_return_an_empty_queue(self):
        queue = Queue()

        expected = 0
        actual = queue.size()

        self.assertEqual(actual, expected)

    def test_should_insert_an_item(self):
        queue = Queue()

        queue.enqueue("eva")

        expected = 1
        actual = queue.size()

        self.assertEqual(actual, expected)

    def test_should_dequeue_an_item(self):
        queue = Queue()

        queue.enqueue("Buzik")
        queue.enqueue("Rubenushka")

        expected = "Buzik"
        actual = queue.dequeue()

        self.assertEqual(actual, expected)
