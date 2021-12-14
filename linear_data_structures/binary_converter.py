#!/usr/bin/python
from stack import Stack

def to_binary(number):
    stack = Stack()
    num = number
    while num > 0:
        rem = num % 2
        stack.push(rem)
        num = num // 2

    binary_string = ""
    while not stack.is_empty():
        digit = stack.pop()
        binary_string = binary_string + str(digit)

    return binary_string

def base_converter(number, base):
    digits = "0123456789ABCDEF"
    stack = Stack()
    num = number
    while num > 0:
        rem = num % base
        stack.push(rem)
        num = num // base

    result_string = ""
    while not stack.is_empty():
        digit = stack.pop()
        result_string = result_string + digits[digit]

    return result_string

if __name__ == '__main__':
    print(base_converter(256, 16))
