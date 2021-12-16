#!/usr/bin/python
def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

# TODO:
# Implement other methods like /, -, *, <, >
class Fraction:
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common
    # Ex 1
    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den

        return Fraction(new_num, new_den)
    # Ex 3
    # https://www.mathsisfun.com/algebra/fractions-algebra.html
    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den

        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den

        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num

        return Fraction(new_num, new_den)
    # Ex 4
    # https://www.mathsisfun.com/comparing-fractions.html
    def __gt__(self, other):
        self_num = self.num * other.den
        other_num = other.num * self.den

        if self_num >= other_num:
            return self
        else:
            return other

    def __ge__(self, other):
        self_num = self.num * other.den
        other_num = other.num * self.den

        if self_num >= other_num:
            return self
        else:
            return other

    def __lt__(self, other):
        self_num = self.num * other.den
        other_num = other.num * self.den

        if self_num < other_num:
            return self
        else:
            return other

    def __le__(self, other):
        self_num = self.num * other.den
        other_num = other.num * self.den

        if self_num <= other_num:
            return self
        else:
            return other

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num

        return first_num == second_num
