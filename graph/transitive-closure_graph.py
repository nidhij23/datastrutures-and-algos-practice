from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.tc = [[0 for j in range(self.V)] for i in range(self.V)]

    def add_edge(self, src, des):
        self.graph[src].append(des)

    def DFSUtil(self, s, v):
        self.tc[s][v]=1
        for i in self.graph[v]:
            if self.tc[s][i]==0:
                self.DFSUtil(s,i)


    def findTc(self):
        for i in range(self.V):
            self.DFSUtil(i,i)
        print(self.tc)


if __name__ == "__main__":

    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.findTc()
