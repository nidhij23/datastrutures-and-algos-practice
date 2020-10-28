from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, des):
        self.graph[src].append(des)

    def BFS(self, src):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(src)
        visited[src] = True
        while queue:
            temp = queue.pop(0)
            print(temp, end=" ")
            for i in self.graph[temp]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(g.BFS(2))

    #Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph
