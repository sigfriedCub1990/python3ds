#!/usr/bin/python
import turtle
import numpy as np

PART_OF_PATH = "O"
TRIED = "."
OBSTACLE = "+"
DEAD_END = "-"

class Maze:
    def __init__(self, file):
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []
        maze_file = open(file, "r")
        rows_in_maze = 0
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == "S":
                    self.start_row = rows_in_maze
                    self.start_col = col
                col = col + 1
            rows_in_maze = rows_in_maze + 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)

        print(np.matrix(self.maze_list))
        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.x_translate = -columns_in_maze / 2
        self.y_translate = rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(
            -(columns_in_maze - 1) / 2 - 0.5,
            -(rows_in_maze - 1) / 2 - 0.5,
            (columns_in_maze - 1) / 2 + 0.5,
            (rows_in_maze - 1) / 2 + 0.5,
        )

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate, -y + self.y_translate, "orange"
                    )
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None

        if color:
            self.drop_bread_crumb(color)

    def is_exit(self, row, col):
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.columns_in_maze - 1
        )

    def __getitem__(self, idx):
        """Overloads [] operator, allowing maze[start_row][end_row]"""
        return self.maze_list[idx]

def search_from(maze, start_row, start_column):
    """Search each of four directions until we find a way out (if any)"""
    maze.update_position(start_row, start_column)
    # Base case #1: We hit a wall
    if maze[start_row][start_column] == OBSTACLE:
        return False
    # Base case #2: We already tried this square
    if (
        maze[start_row][start_column] == TRIED or
        maze[start_row][start_column] == DEAD_END
    ):
        return False
    # Base case #3: We found the exit!
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_column, TRIED)
    # Otherwise try each direction
    found = (
        search_from(maze, start_row, start_column - 1) # West
        or search_from(maze, start_row, start_column + 1) # East
        or search_from(maze, start_row - 1, start_column) # North
        or search_from(maze, start_row + 1, start_column) # South
    )
    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found

if __name__ == '__main__':
    my_maze = Maze("maze.in")
    my_maze.draw_maze()
    my_maze.update_position(my_maze.start_row, my_maze.start_col)

    search_from(my_maze, my_maze.start_row, my_maze.start_col)
