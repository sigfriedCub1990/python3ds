# Queue ADT methods
# - Queue()
# - enqueue(item)
# - dequeue()
# - is_empty()
# - size()

# NOTE.1: I believe this is better if we use a Linked List, well, it has it's downsides, i.e.
# inserting will be O(1), currently is O(n) and poping will be O(n). They are reversed, I think
# this depends for what purposes we want to use the Queue.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def is_empty(self):
        return not bool(self.queue)

    def size(self):
        return len(self.queue)
