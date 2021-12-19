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
# Make append operation O(1)
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


    """ Appends an item to the list """
    def append(self, value):
        if self.head is not None:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value)

    """ Insert an item into index """
    def insert(self, index, value):
        size = self.size()
        if index > size:
            raise IndexError("{} index does not exist".format(index))
        if self.head is None and index != 0:
            raise RuntimeError("There are no elements in the list")
        elif self.head is None and index == 0:
            self.head = Node(value)
        else:
            """
            [1, 2, 3]
            idx 0, item 4 - [4, 1, 2, 3]
            idx 1, item 4 - [1, 4, 2, 3]
            idx 2, item 4 - [1, 2, 4, 3]
            """
            current = self.head
            prev = None
            idx = 0
            while idx != index:
                prev = current
                current = current.next
                idx += 1
            if prev is not None:
                node = Node(value)
                node.next = current
                prev.next = node
            else:
                node = Node(value)
                node.next = current
                self.head = node

    """ Return the index of an item """
    def index(self, value):
        idx = 0
        current = self.head
        # Will fail is list is empty
        while current.data != value or current != None:
            current = current.next
            idx += 1
        if current == None:
            raise ValueError("{} item not in the list".format(value))
        else:
            return idx

    """ Pop item in index """
    def pop(self, index):
        if self.head is None:
            raise RuntimeException("Can not pop an empty list")
        if index > self.size():
            raise IndexError("{} index does not exist".format(index))
        prev = None
        current = self.head
        idx = 0
        while idx != index:
            prev = current
            current = current.next
            idx += 1
        if prev == None:
            value = self.head.data
            self.head = current.next
            return value
        else:
            value = current.data
            prev.next = current.next
            current.next = None
            return value

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

    def __str__(self):
        res = ""
        current = self.head
        while current != None:
            res += f"{str(current.data)} "
            current = current.next
        return res
