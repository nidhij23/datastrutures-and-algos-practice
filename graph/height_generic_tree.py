if __name__ == "__main__":
    # parent = [-1, 0, 0, 0, 3, 1, 1, 2]
    parent = [-1, 0, 1, 2, 3]
    height = [0] * len(parent)

    for i in range(len(parent)):
        if parent[i] == -1:
            height[i] = 0
        else:
            height[i] = height[parent[i]]+1

    print(max(height))
