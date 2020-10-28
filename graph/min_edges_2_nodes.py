from collections import defaultdict


class Graph:

    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_min_edges(self, u, v):
        visited = [0] * self.V
        distance = [0] * self.V
        queue = []
        distance[u] = 0
        queue.append(u)
        visited[u] = True
        while (queue):
            temp = queue.pop(0)
            for child in self.graph[temp]:
                if visited[child] == False:
                    distance[child] = distance[temp] + 1
                    queue.append(child)
                    visited[child] = True
        return distance[v]


if __name__ == "__main__":
    g = Graph(9)
    g.addEdge(0, 1)
    g.addEdge(0, 7)
    g.addEdge(1, 7)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    g.addEdge(2, 8)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 7)
    g.addEdge(7, 8)

    print(g.find_min_edges(0, 5))
