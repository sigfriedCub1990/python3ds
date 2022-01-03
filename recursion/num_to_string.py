#!/usr/bin/python

def to_str(num, base):
    digits = "0123456789ABDCDEF"
    if num < base:
        return digits[num]
    else:
        return to_str(num // base, base) + str(num % base)

def reverse_string(string):
    if len(string) < 1:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

def is_pal(string):
    if len(string) < 1:
        return True
    else:
        if string[0] == string[len(string) - 1]:
            return is_pal(string[1:len(string)-1])
        else:
            return False

def prepare_string(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += char

    return result

if __name__ == '__main__':
    print("Dec {}".format(to_str(769, 10)))
    print("Hex {}".format(to_str(769, 16)))
    print("Bin {}".format(to_str(769, 2)))

    print(reverse_string("ruben"))
    print(reverse_string("eva"))
    print(reverse_string("buzik"))
    print(reverse_string(""))

    print(is_pal('kayak'))
    print(is_pal('ruben'))
    print(is_pal('wassamassaw'))
    print(is_pal('kanakanak'))
