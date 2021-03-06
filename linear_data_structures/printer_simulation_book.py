#!/usr/bin/python
from random import randrange
from queue import Queue
from fraction import Fraction

class Printer:
    def __init__(self, ppm):
        self.ppm = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining // 2
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None


    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.ppm


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp

# We add a third parameter to control the numbers of students
def simulation(num_seconds, pages_per_minute, num_students):
    printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    fraction = Fraction(num_students * 2, 3600)
    print(f"Task every {fraction} seconds")

    for current_second in range(num_seconds):
        # We doubled the amount of students, thus the time to add new tasks
        # to the queue decreases
        if randrange(1, fraction.get_den() + 1) == fraction.get_den():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            printer.start_next(next_task)

        printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print(
            f"Average Wait {average_wait:6.2f} secs" \
            + f"{print_queue.size():3d} tasks remaining."
        )

if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 10, 20)
