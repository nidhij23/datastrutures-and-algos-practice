from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def displayGraph(self):
        for i in range(self.V):
            print(i, "->", self.graph[i])

    def transposeGraph(self, newGraph):
        for i in range(self.V):
            for child in self.graph[i]:
                newGraph.addEdge(child, i)


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(3, 2)
    g.addEdge(4, 1)
    g.addEdge(4, 3)
    newGraph = Graph(g.V)
    g.displayGraph()
    g.transposeGraph(newGraph)
    newGraph.displayGraph()
