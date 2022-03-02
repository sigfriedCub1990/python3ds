#!/usr/bin/python

from graph import Graph


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for a_vertex in self:
            a_vertex.setColor("white")
            a_vertex.setPred(-1)
        for a_vertex in self:
            if a_vertex.getColor() == "white":
                self.dfs_visit(a_vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.setColor("gray")
        self.time += 1
        start_vertex.setDiscovery(self.time)
        for next_vertex in start_vertex.getConnections():
            if next_vertex.getColor() == "white":
                next_vertex.setPred(start_vertex)
                self.dfs_visit(next_vertex)
        start_vertex.setColor("black")
        self.time += 1
        start_vertex.setFinish(self.time)


if __name__ == "__main__":
    g = DFSGraph()
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
    g.dfs()

    # Topological sort
    verts = [v for v in g]
    verts.sort(key=lambda v: v.getFinish(), reverse=True)
    for v in verts:
        print(f"Vertex {v.getId()} -> {v.getFinish()}")
