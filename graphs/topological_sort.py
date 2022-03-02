#!/usr/bin/python
from dfs import DFSGraph

if __name__ == "__main__":
    g = DFSGraph()
    g.addVertex("3/4 cup mil")
    g.addVertex("1 egg")
    g.addVertex("1 Tbl Oil")
    g.addVertex("1 cup mix")
    g.addVertex("heat syrup")
    g.addVertex("heat griddle")
    g.addVertex("pour 1/4 cup")
    g.addVertex("turn when bubbly")
    g.addVertex("eat")

    g.addEdge("3/4 cup mil", "1 cup mix")
    g.addEdge("1 egg", "1 cup mix")
    g.addEdge("1 Tbl Oil", "1 cup mix")
    g.addEdge("1 cup mix", "pour 1/4 cup")
    g.addEdge("1 cup mix", "heat syrup")
    g.addEdge("heat griddle", "pour 1/4 cup")
    g.addEdge("pour 1/4 cup", "turn when bubbly")
    g.addEdge("turn when bubbly", "eat")
    g.addEdge("heat syrup", "eat")
    g.dfs()

    # Topological sort
    verts = [v for v in g]
    verts.sort(key=lambda v: v.getFinish(), reverse=True)
    for v in verts:
        print(f"{v.getId()} {v.getDiscovery()}/{v.getFinish()}")
