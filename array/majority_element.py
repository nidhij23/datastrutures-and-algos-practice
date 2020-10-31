class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1


class BST():
    def __init__(self):
        self.root = None

    def insert(self, data, n):
        print("inserting", data)
        out = None
        if (self.root == None):
            self.root = Node(data)
        else:
            out = self.insertNode(self.root, data, n)
        return out

    def insertNode(self, currentNode, data, n):
        if currentNode.data == data:
            currentNode.count += 1
            if currentNode.count > n / 2:
                return currentNode.data
            else:
                return None
        elif (currentNode.data < data):
            if currentNode.right:
                self.insertNode(currentNode.right, data, n)
            else:
                currentNode.right = Node(data)
        elif (currentNode.data > data):
            if currentNode.left:
                self.insertNode(currentNode.left, data, n)
            else:
                currentNode.left = Node(data)


if __name__ == "__main__":
    arr = [3, 2, 3]
    n = len(arr)
    tree = BST()
    flag = 0
    for i in range(n):
        out = tree.insert(arr[i], n)
        print("out",out)
        if out != None:
            print(arr[i])
            flag = 1
            break
    # print(flag)
