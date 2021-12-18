# Deque ADT
# Deque()
# add_front(item)
# add_rear(item)
# remove_front()
# remove_rear()
# is_emtpy()
# size()

class Deque:
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return not bool(self.deque)

    def add_front(self, item):
        self.deque.append(item)

    def add_rear(self, item):
        self.deque.insert(item, 0)

    def remove_front(self):
        return self.deque.pop()

    def remove_rear(self):
        return self.deque.pop(0)

    def is_empty(self):
        return len(self.deque) != 0

    def size(self):
        return len(self.deque)

    def __str__(self):
        return "".join(self.deque)
