#!/usr/bin/python


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return f"{str(self.id)} connected to: {str([x.id for x in self.connectedTo])}"

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class AugmentedVertex(Vertex):
    def __init__(self, key):
        super().__init__(key)
        self.distance = 0
        self.predecessor = None
        self.color = "white"
        self.discovery = 0
        self.finish = 0

    def setDistance(self, newDistance):
        self.distance = newDistance

    def setPred(self, newPredecessor):
        self.predecessor = newPredecessor

    def setColor(self, newColor):
        self.color = newColor

    def setDiscovery(self, discoveryTime):
        self.discovery = discoveryTime

    def setFinish(self, finishTime):
        self.finish = finishTime

    def getDistance(self):
        return self.distance

    def getPred(self):
        return self.predecessor

    def getColor(self):
        return self.color

    def getFinish(self):
        return self.finish

    def getDiscovery(self):
        return self.discovery

    def __gt__(self, other):
        return self.distance > other.distance

    def __lt__(self, other):
        return self.distance < other.distance


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key) -> Vertex:
        self.numVertices += 1

        newVertex = AugmentedVertex(key)
        self.vertList[key] = newVertex

        return newVertex

    def getVertex(self, n) -> Vertex | None:
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, _from, to, weight=0):
        if _from not in self.vertList:
            self.addVertex(_from)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[_from].addNeighbor(self.vertList[to], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
    for v in g:
        for w in v.getConnections():
            print(
                f"({v.getId()}, {w.getId()}, distance: {v.getDistance()}, pred: {v.getPredecessor()})"
            )
