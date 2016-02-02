class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise RuntimeError('Stack is empty')

        temp_node = self.head
        self.head = self.head.next
        del temp_node

    def printStack(self):
        temp_node = self.head

        while temp_node is not None:
            print temp_node.data
            temp_node = temp_node.next

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.printStack()

stack.pop()

stack.printStack()