#!/usr/bin/python
from queue import Queue

def hot_potato_simulation(names, num):
    sim_queue = Queue()

    # Add names to the queue
    for name in names:
        sim_queue.enqueue(name)

    # While we have children
    while sim_queue.size() > 1:
        # Count num-times and after that...
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        # Remove the kid in the front
        sim_queue.dequeue()

    # Last child
    return sim_queue.dequeue()

if __name__ == '__main__':
    print(hot_potato_simulation([ "bill", "david", "susan", "Jane", "kent", "brad" ], 7))
