from collections import defaultdict


class Deque:
    def __init__(self, size):
        self.arr = defaultdict()
        self.size = size
        self.front = -1
        self.rear = 0

    def isFull(self):
        return self.front == 0 and self.rear == self.size - 1

    def isEmpty(self):
        return self.front == -1

    def insertFront(self, key):
        if self.isFull():
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0

        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front = self.front - 1
        print("Inserted at front", key)
        self.arr[self.front] = key

    def insertRear(self, key):
        if self.isFull():
            print("Overflow")
            return
        if self.front == -1:
            self.front = self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear = self.rear + 1
        print("self.rear", self.rear)
        print("Inserted at rear", key)
        self.arr[self.rear] = key

    def deleteFront(self):
        if self.isEmpty():
            print("Queue Underflow")
        print("deleting from front")
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            if self.front == self.size - 1:
                self.front = 0
            else:
                self.front = self.front + 1

    def deleteRear(self):
        if self.isEmpty():
            print("Overflow")
            return
        print("deleting from rear")
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear = self.rear - 1

    def getFront(self):
        if self.isEmpty():
            print("underflow")
            return
        print("Front", self.arr[self.front])

    def getRear(self):
        if self.isEmpty() or self.rear < 0:
            print("Underflow")
            return
        print("Rear", self.arr[self.rear])


if __name__ == "__main__":
    dq = Deque(5)
    print(dq.front)
    print(dq.rear)

    dq.insertRear(5)
    dq.getFront()
    dq.getRear()
    dq.insertRear(10)
    dq.getFront()
    dq.getRear()
    dq.deleteRear()
    dq.getFront()
    dq.getRear()

    dq.insertFront(15)
    dq.getFront()
    dq.getRear()
    dq.deleteFront()
    dq.getFront()
    dq.getRear()
