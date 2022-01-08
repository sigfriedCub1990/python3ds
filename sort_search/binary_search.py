#!/bin/python
list = [1, 2, 3, 4, 5, 10, 13, 15, 20]
#       0,1,2,3,4, 5, 6, 7,8,9


def binary_search(l, item, start, end):
    mid = (start + end) // 2
    if start >= end:
        return False
    elif l[mid] == item:
        return True
    elif l[mid] < item:
        # take upper half
        return binary_search(l, item, mid + 1, end)
    else:
        # take lower half
        return binary_search(l, item, start, mid - 1)


def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return False


if __name__ == "__main__":
    print(binary_search(list, 2, 0, len(list)))
    print(binary_search_iterative(list, 2))
    print(binary_search(list, 26, 0, len(list)))
