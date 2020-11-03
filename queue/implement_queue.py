class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = self.size = 0
        self.Q = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("%s enqueud to queue" % str(item))

    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return
        print("% s dequeud from queue", self.Q[self.front])
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1

    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Front item is %s" % str(self.Q[self.front]))

    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is %s" % str(self.Q[self.rear]))


if __name__ == "__main__":
    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.EnQueue(50)
    queue.DeQueue()
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()
