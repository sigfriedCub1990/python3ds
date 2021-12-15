# Stack ADT methods
# - Stack()
# - pop()
# - push()
# - peek()
# - is_empty()
# - size()
class Stack:
    """
        Stack data structure using
        built-in Python lists
    """
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack.pop()
        return item

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise RuntimeError('Can not peek from an empty Stack')
