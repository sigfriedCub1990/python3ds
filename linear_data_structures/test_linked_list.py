import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_should_construct_empty_list(self):

        expected = None
        actual = self.list.head

        self.assertEqual(actual, expected)

    def test_should_add_an_item(self):

        self.list.add(1)

        expected = "1"
        actual = str(self.list.head)

        self.assertEqual(actual, expected)

    def test_should_return_list_size(self):

        self.list.add(1)
        self.list.add(2)

        expected = 2
        actual = self.list.size()

        self.assertEqual(actual, expected)

    def test_should_find_element(self):
        self.list.add(4)
        self.list.add(5)
        self.list.add(6)

        expected_one = 6
        expected_two = 5

        actual_one = self.list.search(6).data
        actual_two = self.list.search(5).data

        self.assertEqual(actual_one, expected_one)
        self.assertEqual(actual_two, expected_two)

    def test_should_return_none_if_not_found(self):
        self.list.add(7)
        self.list.add(8)

        expected = None
        actual = self.list.search(10)

        self.assertEqual(actual, expected)

    def test_should_append_an_item(self):
        self.list.add(1)
        self.list.append(2)

        expected = 1
        actual = self.list.head.data

        self.assertEqual(actual, expected)

    def test_should_append_if_no_head(self):
        self.list.append(1)

        expected = 1
        actual = self.list.head.data

        self.assertEqual(actual, expected)
