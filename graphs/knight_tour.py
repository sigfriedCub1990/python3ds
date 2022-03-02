#!/usr/bin/python

from typing import List
from graph import Graph


def knight_graph(bd_size):
    """
    Generates a Graph with all the possible moves of the Knight in a board
    of give size

    bd_size: Size of the board
    """
    kt_graph = Graph()
    for row in range(bd_size):
        for col in range(bd_size):
            node_id = pos_to_node_id(row, col, bd_size)
            new_positions = gen_legal_moves(row, col, bd_size)
            for e in new_positions:
                nid = pos_to_node_id(e[0], e[1], bd_size)
                kt_graph.addEdge(node_id, nid)
    return kt_graph


def pos_to_node_id(row, column, board_size):
    """
    Translates the position [row, column] into
    a node_id (linear representation) of the
    give position

    row: Row the Knight is in
    column: Column the Knight is in
    board_size: Size of the board
    """
    return (row * board_size) + column


def gen_legal_moves(row: int, col: int, bd_size: int) -> List:
    """
    Generates all the legal moves form a given position [row, col]
    in a board of size bd_size
    """
    new_moves = []
    move_offsets = [
        (-1, -2),
        (-1, 2),
        (-2, -1),
        (-2, 1),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]
    for move in move_offsets:
        new_x = row + move[0]
        new_y = col + move[1]
        if is_legal_coord(new_x, bd_size) and is_legal_coord(new_y, bd_size):
            new_moves.append((new_x, new_y))
    return new_moves


def is_legal_coord(x, bd_size):
    """Determines if current position is legal or not"""
    return x >= 0 and x < bd_size


def order_by_avail(n):
    """
    Order the available squares you can move to by the
    number of possible moves from that square.

    NOTE: This is an heuristic called Warnsdorff's algorithm
    """
    res_list = []
    for v in n.getConnections():
        if v.getColor() == "white":
            c = 0
            for w in v.getConnections():
                if w.getColor() == "white":
                    c = c + 1
            res_list.append((c, v))
    res_list.sort(key=lambda x: x[0])
    return [y[1] for y in res_list]


def knight_tour(n, path, u, limit):
    u.setColor("gray")
    path.append(u)
    if n < limit:
        nbr_list = list(
            u.getConnections()
        )  # To use heuristic just use order_by_avail instead
        # nbr_list = order_by_avail(u)
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].getColor() == "white":
                done = knight_tour(n + 1, path, nbr_list[i], limit)
            i = i + 1
        if not done:
            path.pop()  # Ready to backtrack
            u.setColor("white")
    else:
        done = True
    return done


if __name__ == "__main__":
    g = Graph()
    g.addVertex("a")
    g.addVertex("b")
    g.addVertex("c")
    g.addVertex("d")
    g.addVertex("e")
    g.addVertex("f")
    g.addEdge("a", "b")
    g.addEdge("a", "d")
    g.addEdge("b", "c")
    g.addEdge("b", "d")
    g.addEdge("d", "e")
    g.addEdge("e", "b")
    g.addEdge("e", "f")
    g.addEdge("f", "c")
    # Knight's tour
    path = []
    initial_vertex = g.getVertex("a")
    limit = 6
    n = 1
    knight_tour(n, path, initial_vertex, limit)
    solution = []
    for v in path:
        solution.append(v.getId())
    print(f"Solution: {solution}")
