#!/usr/bin/env python


def modexp(x, n, p):
    if n == 0:
        return 1
    t = (x * x) % p
    tmp = modexp(t, n // 2, p)
    if n % 2 != 0:
        tmp = (tmp * x) % p
    return tmp


def gcd_naive(a, b):
    """Easy but inefficient for a >> b"""
    if b == 0:
        return a
    elif a < b:
        return gcd_naive(b, a)
    return gcd_naive(a - b, b)


def gcd_improved(a, b):
    """
    Better since we exploit the fact that a -b < b is really the same as
    a divided by b
    """
    if b == 0:
        return a
    return gcd_improved(a, a % b)


def ext_gcd(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = ext_gcd(y, x % y)
        return (d, b, a - (x // y) * b)


if __name__ == "__main__":
    # TODO: For fun time the GCD functions
    res = ext_gcd(25, 9)
    print(f"Result: {res}")
