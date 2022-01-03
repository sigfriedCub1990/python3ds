#!/usr/bin/python

def solve_hanoi(height, from_pole, to_pole, with_pole):
    if height >= 1:
        solve_hanoi(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        solve_hanoi(height -1, with_pole, to_pole, from_pole)

def move_disk(from_p, to_p):
    print("moving disk from {} to {}".format(from_p, to_p))

if __name__ == '__main__':
    solve_hanoi(3, "initial", "helper", "final")
