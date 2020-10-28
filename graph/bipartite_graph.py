from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.graph = [[0 for column in range(V)]
                      for row in range(V)]
        self.V = V

    def isBipartite(self, src):
        colorArr = [-1] * self.V

        colorArr[src] = 1
        queue = []
        queue.append(src)
        while queue:
            u = queue.pop()
            if self.graph[u][u] == 1:
                return False
            for v in range(self.V):
                if self.graph[u][v] == 1 and colorArr[v] == -1:
                    colorArr[v] = 1 - colorArr[u]
                    queue.append(v)
                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                    return False
        print(colorArr)
        return True


if __name__ == "__main__":
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]
               ]
    if g.isBipartite(0):
        print("Yes")
    else:
        print("No")
