from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, des):
        self.graph[src].append(des)
        # self.graph[des].append(src)

    def DFSUtil(self, node, visited):
        visited[node] = True
        print(node, end=" ")
        for i in self.graph[node]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, node):
        visited = [False] * (len(self.graph))
        self.DFSUtil(node, visited)
    # print(stack)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.DFS(0)
