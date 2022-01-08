#!/bin/python
from timeit import Timer
from random import sample

from bubble_sort import bubble_sort_short, bubble_sort
from merge_sort import merge_sort
from quicksort import quick_sort, quick_sort_book
from shell_sort import shell_sort

MAX_ITEMS = 2_000
COUNTER = 9_00

l = sample(range(1, MAX_ITEMS), k=COUNTER)
m = l.copy()
n = l.copy()
o = l.copy()
p = l.copy()
q = l.copy()


def test_quicksort_book():
    quick_sort_book(p)


def test_dummy_bubble():
    bubble_sort(o)


def test_bubble():
    bubble_sort_short(l)


def test_quicksort():
    quick_sort(m)


def test_mergesort():
    merge_sort(n)


def test_shell_sort():
    shell_sort(q)


if __name__ == "__main__":
    t1 = Timer("test_quicksort()", setup="from __main__ import test_quicksort")
    print(f"quick_sort: {t1.timeit(number=1000):15.2f} milliseconds")
    t5 = Timer(
        "test_quicksort_book()", setup="from __main__ import test_quicksort_book"
    )
    print(f"book quick sort: {t5.timeit(number=1000):10.2f} milliseconds")
    t2 = Timer("test_bubble()", setup="from __main__ import test_bubble")
    print(f"short bubble sort: {t2.timeit(number=1000):8.2f} milliseconds")
    t3 = Timer("test_mergesort()", setup="from __main__ import test_mergesort")
    print(f"merge_sort: {t3.timeit(number=1000):15.2f} milliseconds")
    t4 = Timer("test_dummy_bubble()", setup="from __main__ import test_dummy_bubble")
    print(f"dummy bubble sort: {t4.timeit(number=1000):8.2f} milliseconds")
    t5 = Timer("test_shell_sort()", setup="from __main__ import test_shell_sort")
    print(f"test shell sort: {t5.timeit(number=1000):8.2f} milliseconds")
