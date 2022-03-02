#!/usr/bin/env python3

import sys
from pythonds3 import PriorityQueue
from graph import Graph


def prim(g):
    pq = PriorityQueue()
    pq.heapify([(v.getDistance(), v) for v in g])
    while not pq.is_empty():
        (_, current_vert) = pq.delete()
        for next_vert in current_vert.getConnections():
            new_cost = current_vert.getDistance() + current_vert.getWeight(next_vert)
            if next_vert in pq and new_cost < next_vert.getDistance():
                next_vert.setPred(current_vert)
                next_vert.setDistance(new_cost)
                pq.change_priority(next_vert, new_cost)


def find_min_path(graph, to):
    min_path = []
    current = graph.getVertex(to)
    while current is not None:
        min_path.append(current.getId())
        current = current.getPred()
    return min_path


if __name__ == "__main__":
    g = Graph()
    for key in 'ABCDEFG':
        g.addVertex(key)
    for v in g:
        v.setDistance(sys.maxsize)
    g.addEdge('A', 'B', 2)
    g.addEdge('A', 'C', 3)
    g.addEdge('B', 'A', 2)
    g.addEdge('B', 'C', 1)
    g.addEdge('B', 'D', 1)
    g.addEdge('B', 'E', 4)
    g.addEdge('C', 'B', 1)
    g.addEdge('C', 'A', 3)
    g.addEdge('C', 'F', 5)
    g.addEdge('D', 'B', 1)
    g.addEdge('D', 'E', 1)
    g.addEdge('E', 'D', 1)
    g.addEdge('E', 'B', 4)
    g.addEdge('E', 'F', 1)
    g.addEdge('F', 'C', 5)
    g.addEdge('F', 'E', 1)
    g.addEdge('F', 'G', 1)
    g.addEdge('G', 'F', 1)

    g.getVertex('A').setDistance(0)
    prim(g)
    for v in g:
        print(f"Distance to {v.getId()} is {v.getDistance()}")
    print(find_min_path(g, 'G'))
