#!/usr/bin/python
from timeit import Timer

def f1():
    l = []
    for i in range(1000):
        l = l + [i]

def f2():
    l = []
    for i in range(1000):
        l.append(i)

def f3():
    l = [i for i in range(1000)]

def f4():
    l = list(range(1000))

def empty():
    pass

t1 = Timer("f1()", "from __main__ import f1")
print(f"concatenation: {t1.timeit(number=1000):15.2f} milliseconds")
t2 = Timer("f2()", "from __main__ import f2")
print(f"appending: {t2.timeit(number=1000):19.2f} milliseconds")
t3 = Timer("f3()", "from __main__ import f3")
print(f"list comprehension: {t3.timeit(number=1000):10.2f} milliseconds")
t4 = Timer("f4()", "from __main__ import f4")
print(f"list range: {t4.timeit(number=1000):18.2f} milliseconds")
t5 = Timer("empty()", "from __main__ import empty")
print(f"empty function: {t5.timeit(number=1000):14.2f} milliseconds")

# Validate hypothesis that pop(0) is O(n) and pop() is O(1)
# by actually performing the operations
pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")
print(f"{'n':10s}{'pop(0)':>15s}{'pop()':>15s}")
for i in range(1_000_000, 100_000_001, 1_000_000):
    x = list(range(i))
    pop_zero_t = pop_zero.timeit(number=1000)
    x = list(range(i))
    pop_end_t = pop_end.timeit(number=1000)
    print(f"{i:<10d}{pop_zero_t:>15.5f}{pop_end_t:>15.5f}")
