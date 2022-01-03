#!/usr/bin/python
import turtle

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


def main():
    turle = turtle.Turtle()
    win = turtle.Screen()
    draw_spiral(turtle, 100)
    win.exitonclick()

if __name__ == "__main__":
    main()
