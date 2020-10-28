from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, des):
        self.graph[src].append(des)

    def DFS(self, node):
        stack = []
        visited = [False] * (len(self.graph))
        stack.append(node)
        visited[node] = True
        while stack:
            temp = stack.pop()
            print(temp , end=" ")
            for i in self.graph[temp]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True


if __name__=="__main__":
    g= Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.DFS(0)