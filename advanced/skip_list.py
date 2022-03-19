#!/usr/bin/env python3

from random import randrange
from pythonds3 import Stack


def flip():
    return randrange(2)


class HeaderNode:
    def __init__(self):
        self._next = None
        self._down = None

    @property
    def next(self):
        return self._next

    @property
    def down(self):
        return self._down

    @next.setter
    def next(self, value):
        self._next = value

    @down.setter
    def down(self, value):
        self._down = value


class DataNode:
    def __init__(self, key, value) -> None:
        self._key = key
        self._value = value
        self._next = None
        self._down = None

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @property
    def down(self):
        return self._down

    @key.setter
    def key(self, value):
        self._key = value

    @value.setter
    def value(self, value):
        self._value = value

    @next.setter
    def next(self, value):
        self._next = value

    @down.setter
    def down(self, value):
        self._down = value


class SkipList:
    def __init__(self) -> None:
        self._head = None

    def search(self, key):
        current = self._head

        while current:
            if current.next == None:
                current = current.down
            else:
                if current.next.key == key:
                    return current.next.data
                else:
                    if key < current.next.key:
                        current = current.down
                    else:
                        current = current.next

        return None

    def insert(self, key, value):
        if self._head == None:
            self._head = HeaderNode()
            temp = DataNode(key, value)
            self._head.next = temp
            top = temp
            while flip() == 1:
                new_head = HeaderNode()
                temp = DataNode(key, value)
                temp.down = top
                new_head.next = temp
                new_head.down = self._head
                self._head = new_head
                top = temp
        else:
            tower = Stack()
            current = self._head
            while current:  # Find position to insert
                if current.next is None:
                    tower.push(current)  # "Remember" where we went down
                    current = current.down
                else:
                    if key < current.next.key:
                        tower.push(current)
                        current = current.down
                    else:
                        current = current.next

            lowest_level = tower.pop()
            temp = DataNode(key, value)
            temp.next = lowest_level.next
            lowest_level.next = temp
            top = temp
            while flip() == 1:
                if tower.is_empty():
                    # If tower is empty this means that the tower has the same depth as the current Skip List
                    # hence we must create a new HeadNode and make it the new _head of the Skip List
                    new_head = HeaderNode()
                    temp = DataNode(key, value)
                    temp.down = top
                    new_head.next = temp
                    new_head.down = self._head
                    self._head = new_head
                    top = temp
                else:
                    next_level = tower.pop()
                    temp = DataNode(key, value)
                    temp.down = top
                    temp.next = next_level.next
                    next_level.next = temp
                    top = temp

    def remove(self, key):
        # TODO
        pass


if __name__ == "__main__":
    pass
