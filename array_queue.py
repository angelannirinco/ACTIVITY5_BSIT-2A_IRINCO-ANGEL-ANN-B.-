class ArrayQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Overflow: Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Underflow: Queue is empty")
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            raise Exception("Underflow: Queue is empty")
        return self.data[self.front]

    def display(self):
        print(f"Queue: {self.data} front={self.front} rear={self.rear} size={self.size}")
