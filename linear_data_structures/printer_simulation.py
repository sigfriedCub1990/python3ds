#!/usr/bin/python
from queue import Queue
from random import randrange
from statistics import mean

def printer_simulation(quality):
    print_queue = Queue()
    waiting_list_times = []
    is_printer_working = False
    seconds_per_page = 0
    if (quality == 0):
        seconds_per_page = 6
    else:
        seconds_per_page = 12
    # Simulate an hour
    for current_second in range(3600):
        # A new task would be created every 180 seconds,
        # if result = 180 a new task is added to the queue
        # with a timestamp
        new_task = randrange(1, 181)
        if new_task == 180:
            print_queue.enqueue(current_second)

        # If print is free and we have something waiting
        # in the queue, let's process it
        if not is_printer_working and print_queue.size() > 0:
            # Process job in queue
            timestamp = print_queue.dequeue()
            print(f"Timestamp: {timestamp}")
            # How many pages will be printed
            pages = randrange(1, 21)
            # How long this job was waiting?
            print(f"Current second: {current_second}")
            waiting_list_times.append(current_second - timestamp)

            # How much time will it take? This depends on quality too
            # Printer prints 10 pages per minute -> 1 / 6 seconds in normal quality
            # Printer prints 5 pages per minute -> 1 / 12 seconds with good quality
            time_to_print = pages * seconds_per_page

            if time_to_print > 0:
                is_printer_working = True # Semaphore ^)
                elapsed_time_while_printing = 0
                while elapsed_time_while_printing < time_to_print:
                    elapsed_time_while_printing += 1
                print(f"Job done in: {elapsed_time_while_printing} seconds")
                current_second += elapsed_time_while_printing
                is_printer_working = False

    print(waiting_list_times)
    return mean(waiting_list_times)

if __name__ == '__main__':
    print(f"Average time for printing (with draft quality): {printer_simulation(0)}")
