class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return False

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Underflow: Queue is empty")
        item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return item

    def peek_front(self):
        if self.is_empty():
            raise Exception("Underflow: Queue is empty")
        return self.head.data

    def display(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(f"Queue: FRONT -> {result} -> REAR")
