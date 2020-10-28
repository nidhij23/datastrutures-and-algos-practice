from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)

    def DFS(self, node, visited):
        visited[node] = True
        for child in self.graph[node]:
            if visited[child] == False:
                self.DFS(child, visited)

    def count_trees(self):
        visited = [False] * self.V
        count = 0
        for i in range(self.V):
            if visited[i] == False:
                self.DFS(i, visited)
                count += 1
        return count


if __name__ == "__main__":
    g = Graph(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(3, 4);
print(g.count_trees())
