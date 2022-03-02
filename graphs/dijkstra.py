#!/usr/bin/env python3

import sys
from pythonds3 import PriorityQueue
from graph import AugmentedVertex, Graph

# Complexity is O((V + E)*log(V))
def dijkstra(graph: Graph, start: AugmentedVertex) -> None:
    pq = PriorityQueue()
    start.setDistance(0)
    pq.heapify([(v.getDistance(), v) for v in graph])  # O(V) complexity
    while not pq.is_empty():  # O(V)
        (_, current_vert) = pq.delete()  # O(log(V))
        # The loop through the queue and delete operations yield
        # a complexity of O(V*log(V))
        for next_vert in current_vert.getConnections():
            new_dist = current_vert.getDistance() + current_vert.getWeight(next_vert)
            if new_dist < next_vert.getDistance():
                next_vert.setDistance(new_dist)
                next_vert.setPred(current_vert)
                # What defines the Node's priority in this case
                # is the distance
                pq.change_priority(next_vert, new_dist)  # O(E*log(V))


def find_min_path(graph, to):
    min_path = []
    current = graph.getVertex(to)
    while current is not None:
        min_path.append(current.getId())
        current = current.getPred()
    return min_path


if __name__ == "__main__":
    graph = Graph()
    for key in range(1, 7):
        graph.addVertex(key)
    graph.addEdge(1, 2, 7)
    graph.addEdge(1, 3, 9)
    graph.addEdge(1, 6, 14)
    graph.addEdge(2, 1, 7)
    graph.addEdge(2, 3, 10)
    graph.addEdge(2, 4, 15)
    graph.addEdge(3, 1, 9)
    graph.addEdge(3, 4, 11)
    graph.addEdge(3, 6, 2)
    graph.addEdge(4, 2, 15)
    graph.addEdge(4, 3, 11)
    graph.addEdge(4, 5, 6)
    graph.addEdge(5, 4, 6)
    graph.addEdge(5, 6, 9)
    graph.addEdge(6, 5, 9)
    graph.addEdge(6, 1, 14)
    graph.addEdge(6, 3, 2)
    for v in graph:
        v.setDistance(sys.maxsize)
    start = graph.getVertex(1)
    # print(graph.getVertex(5).getConnections())
    dijkstra(graph, start)
    # for v in graph:
    #     print(f"{v.getId()} distance is {v.getDistance()}")
    print(find_min_path(graph, 5))
