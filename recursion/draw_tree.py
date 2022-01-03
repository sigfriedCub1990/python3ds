#!/usr/bin/python
#
# Modify the recursive tree program using one or all of the following ideas:
#
#     Modify the thickness of the branches so that as the branch_len gets smaller, the line gets thinner.
#
#     Modify the color of the branches so that as the branch_len gets very short it is colored like a leaf.
#
#     Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.
#
#     Modify the branch_len recursively so that instead of always subtracting the same amount you subtract a random amount in some range.

import turtle

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()

if __name__ == '__main__':
    main()
