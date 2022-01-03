#!/usr/bin/python

def sum_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_list(num_list[1:])

if __name__ == '__main__':
    print(sum_list([1, 3, 5, 7, 9]))
