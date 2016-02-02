class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp_node = self.head

        while temp_node.next is not None:
            temp_node = temp_node.next

        temp_node.next = new_node

    def dequeue(self):
        if self.head is None:
            raise RuntimeError('Queue is empty')

        temp_node = self.head
        self.head = self.head.next
        del temp_node

    def printQueue(self):
        temp_node = self.head

        while temp_node is not None:
            print temp_node.data
            temp_node = temp_node.next

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.printQueue()

queue.dequeue()

queue.printQueue()