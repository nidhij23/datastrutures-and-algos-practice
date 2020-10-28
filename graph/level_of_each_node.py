from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)

    def BFS(self, node, visited):
        if visited[node] == False:
            print(node, end=" ")
            visited[node] = True

            for child in self.graph[node]:
                self.BFS(child, visited)

    def count_nodes_at_level(self, root, k):
        level = [0] * self.V
        queue = []
        count = 0
        # print(level)
        visited = [False] * self.V
        queue.append(root)
        level[root] = 0
        # visited[root] = True
        while (queue):
            print("in while")
            temp = queue.pop(0)
            if visited[temp] == False:
                print("in if false")
                visited[temp] = True
                for child in self.graph[temp]:
                    queue.append(child)
                    level[child] = level[temp] + 1
        for i in range(self.V):
            print("level of", i, " is ", level[i])
            if level[i] == k:
                count += 1
        return count


if __name__ == "__main__":
    g = Graph(8);
    g.add_edge(0, 1);
    g.add_edge(0, 2);
    g.add_edge(1, 3);
    g.add_edge(1, 4);
    g.add_edge(2, 5);
    g.add_edge(2, 6);
    g.add_edge(6, 7);
    print(g.count_nodes_at_level(0, 2))
