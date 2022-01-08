#!/usr/bin/python
from random import randint


def quick_sort(a_list):
    # print(f"Initial list {a_list}")
    quick_sort_helper(a_list, 0, len(a_list) - 1)


def quick_sort_helper(a_list, lo, hi):
    if lo >= 0 and hi >= 0 and lo < hi:
        split = partition(a_list, lo, hi)
        quick_sort_helper(a_list, lo, split)
        quick_sort_helper(a_list, split + 1, hi)


def partition(a_list, lo, hi):
    pivot = a_list[(lo + hi) // 2]
    left_mark = lo - 1
    right_mark = hi + 1

    while True:
        while True:
            left_mark = left_mark + 1
            if a_list[left_mark] >= pivot:
                break
        while True:
            right_mark = right_mark - 1
            if a_list[right_mark] <= pivot:
                break
        if left_mark >= right_mark:
            return right_mark
        a_list[left_mark], a_list[right_mark] = (
            a_list[right_mark],
            a_list[left_mark],
        )


def quick_sort_book(a_list):
    quick_sort_helper_book(a_list, 0, len(a_list) - 1)


def quick_sort_helper_book(a_list, first, last):
    if first < last:
        split = partition_book(a_list, first, last)
        quick_sort_helper_book(a_list, first, split - 1)
        quick_sort_helper_book(a_list, split + 1, last)


def partition_book(a_list, first, last):
    pivot_val = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            left_mark = left_mark + 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = (
                a_list[right_mark],
                a_list[left_mark],
            )
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    return right_mark


if __name__ == "__main__":
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 34]
    # a_list = [4, 3, 2, 1]
    # a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # a_list = [9, 11, 3, 1, 42]
    # a_list = [randint(1, 50) for _ in range(7)]
    # a_list = [20, 45, 31, 46, 34, 32, 31]
    # a_list = [3, 1, 1]
    a_list = [randint(1, 1_000_000) for _ in range(1_000_000)]
    quick_sort(a_list)
    print(f"Sorted list: {a_list}")
