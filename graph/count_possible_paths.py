from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def count_possible_paths_helper(self, src, des, visted, pathcount):
        visted[src] = True
        if src == des:
            pathcount[0] += 1
        else:
            for child in self.graph[src]:
                if visted[child] == False:
                    self.count_possible_paths_helper(child, des, visted, pathcount)
        visted[src] = False


    def count_possible_paths(self, src, des):
        visited = [False] * self.V
        pathcount = [0]
        self.count_possible_paths_helper(src, des, visited, pathcount)
        return pathcount[0]


if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    print(g.count_possible_paths(2, 3))
