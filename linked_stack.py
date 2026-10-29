class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return False

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Underflow: Stack is empty")
        item = self.head.data
        self.head = self.head.next
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Underflow: Stack is empty")
        return self.head.data

    def display(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(f"Stack: {result} <- top")
