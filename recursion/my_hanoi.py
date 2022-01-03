#!/usr/bin/python
def move(from_p, to_p):
    print("Moving from {} to {}".format(from_p, to_p))

# You don't need to remember this function,
# remember, you can always remember this
# by working backwards, as recursion will
# do
# TODO: I should write about this in order
# to really consolidate and of course
# quote Computerphile for their great and
# funny explanation. Keep going!
def hanoi(n, initial, helper, final):
    if n >= 1:
        hanoi(n - 1, initial, final, helper)
        move(initial, final)
        hanoi(n - 1, helper, initial, final)

if __name__ == '__main__':
    hanoi(3, "initial", "helper", "final")
