#!/usr/bin/python
from graph import Graph

# Investigate how to define modules in a
# way I can import this from linear_data_structures
# folder
from queue import Queue


def buildGraph(wordFile):
    d = {}
    g = Graph()
    with open(wordFile, "r") as f:
        # create buckets for words that differ by one letter
        # e.g. _ale, p_le, pa_e, pal_ for the word pale
        for line in f:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + "_" + word[i + 1 :]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
        # add vertices and edges for words in the same bucket
        print(d.keys())
        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.addEdge(word1, word2)
        return g


def bfs(g, start):
    """Breadth First Search"""
    q = Queue()
    q.enqueue(start)
    while q.size() > 0:
        currentVert = q.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == "white":
                nbr.setColor("gray")
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                q.enqueue(nbr)
        currentVert.setColor("black")


def traverse(y):
    """
    From a Node go all the way back until the
    beggining of the Graph
    """
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())


if __name__ == "__main__":
    g = buildGraph("words.txt")
    start = g.getVertex("fool")
    bfs(g, start)
    traverse(g.getVertex("sage"))
    # print(f"distance to sage: {g.getVertex('sage').getPred().id}")
