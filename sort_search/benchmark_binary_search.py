#!/usr/bin/python
from timeit import Timer
from random import sample
from quicksort import quick_sort
from binary_search import binary_search, binary_search_iterative

MAX_ITEMS = 9_000
COUNTER = 8_000

l = sample(range(1, MAX_ITEMS), k=COUNTER)
quick_sort(l)


def test_binary_recursive():
    binary_search(l, 4, 0, len(l) - 1)


def test_binary_iterative():
    binary_search_iterative(l, 4)


if __name__ == "__main__":
    t1 = Timer(
        "test_binary_iterative()", setup="from __main__ import test_binary_iterative"
    )
    print(f"iterative binary search: {t1.timeit(number=1000):15.2f} milliseconds")
    t2 = Timer(
        "test_binary_recursive()", setup="from __main__ import test_binary_recursive"
    )
    print(f"recursive binary search: {t2.timeit(number=1000):15.2f} milliseconds")
