#!/bin/python


def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        idx = i
        for cur_pos in range(i, 0, -1):
            if a_list[cur_pos - 1] > cur_val:
                a_list[cur_pos] = a_list[cur_pos - 1]
                idx = cur_pos - 1
            else:
                break
        a_list[idx] = cur_val


if __name__ == "__main__":
    l = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(l)
    print(l)
