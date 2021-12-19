class Node:
    def __init__(self, value):
        self._data = value
        self._next = None

    def get_data(self):
        return self._data

    def set_data(self, value):
        self._data = value

    data = property(get_data, set_data)

    def get_next(self):
        return self._next

    def set_next(self, next):
        self._next = next

    next = property(get_next, set_next)

    def __str__(self):
        return str(self._data)



# TODO:
# Implement append, insert, index and pop
class LinkedList:
    """
    Linked List using Node CS 101
    """
    def __init__(self):
        self.head = None

    """ Returns if list is empty or not """
    def is_empty(self):
        return self.head == None

    """ Adds an item to the list """
    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        if self.head is not None:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value)

    """ Return the size of the list """
    def size(self):
        count = 0
        current = self.head
        while (current != None):
            count += 1
            current = current.next
        return count

    """
    Search an item in the list and returns it,
    if item not found returns None
    """
    def search(self, value):
        current = self.head
        while (current != None):
            if current.data == value:
                return current
            else:
                current = current.next
        return None

    """
    Removes an item from the list or throws
    a ValueError exception if item is not
    in the list
    """
    def remove(self, value):
        current = self.head
        previous = None

        while current is not None:
            if current.data == value:
                break
            previous = current
            current = current.next
        if current is None:
            raise ValueError("{} is not in the list".format((value)))
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
