from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, k, vDegrees, visited):
        visited[v] = True
        for i in self.graph[v]:
            if vDegrees[v] < k:
                vDegrees[i] = vDegrees[i] - 1
            if visited[i] == False:
                if self.DFSUtil(i, k, vDegrees, visited):
                    vDegrees[v] -= 1
        return vDegrees[v] < k

    def printKCores(self, k):
        visited = [False] * (self.V)
        vDegrees = [0] * (self.V)
        for i in self.graph:
            vDegrees[i] = (len(self.graph[i]))

        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i, k, vDegrees, visited)

        for v in range(self.V):
            if vDegrees[v] >= k:
                print(str("\n [ ") + str(v) + str(" ]"), )
                for i in self.graph[v]:
                    if vDegrees[i] >= k:
                        print("-> " + str(i), )


if __name__ == "__main__":
    k = 3;
    g1 = Graph(9);
    g1.addEdge(0, 1)
    g1.addEdge(0, 2)
    g1.addEdge(1, 2)
    g1.addEdge(1, 5)
    g1.addEdge(2, 3)
    g1.addEdge(2, 4)
    g1.addEdge(2, 5)
    g1.addEdge(2, 6)
    g1.addEdge(3, 4)
    g1.addEdge(3, 6)
    g1.addEdge(3, 7)
    g1.addEdge(4, 6)
    g1.addEdge(4, 7)
    g1.addEdge(5, 6)
    g1.addEdge(5, 8)
    g1.addEdge(6, 7)
    g1.addEdge(6, 8)
    # print(g1)
    print((g1.V))
    # print(g1.graph)
    g1.printKCores(k)

    # g2 = Graph(13);
    # g2.addEdge(0, 1)
    # g2.addEdge(0, 2)
    # g2.addEdge(0, 3)
    # g2.addEdge(1, 4)
    # g2.addEdge(1, 5)
    # g2.addEdge(1, 6)
    # g2.addEdge(2, 7)
    # g2.addEdge(2, 8)
    # g2.addEdge(2, 9)
    # g2.addEdge(3, 10)
    # g2.addEdge(3, 11)
    # g2.addEdge(3, 12)
    # g2.printKCores(k)
