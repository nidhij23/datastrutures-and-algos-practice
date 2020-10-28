def dfs(adj, node, parent, color):
    count_color[color] += 1
    for i in range(len(adj[node])):
        if adj[node][i] != parent:
            dfs(adj, adj[node][i], node, not color)


def findMaxEdges(adj, n):
    dfs(adj, 1, 0, 0)
    return count_color[0] * count_color[1] - (n - 1)


if __name__ == "__main__":
    count_color = [0, 0]
    n = 5
    adj = [[] for i in range(n + 1)]
    adj[1].append(2)
    adj[1].append(3)
    adj[2].append(4)
    adj[3].append(5)

    print(findMaxEdges(adj, n))
    print(count_color)
