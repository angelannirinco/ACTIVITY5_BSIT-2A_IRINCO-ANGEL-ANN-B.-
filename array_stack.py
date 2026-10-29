class ArrayStack:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise Exception("Overflow: Stack is full")
        self.top += 1
        self.data[self.top] = item

    def pop(self):
        if self.is_empty():
            raise Exception("Underflow: Stack is empty")
        item = self.data[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Underflow: Stack is empty")
        return self.data[self.top]

    def display(self):
        print(f"Stack: {self.data[:self.top+1]}")
