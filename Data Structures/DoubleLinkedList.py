class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def addToHead(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            raise RuntimeError('List is empty')

        temp_node = self.find(data)

        if temp_node is None:
            print 'Did not find', data
            return

        # Node is head
        if temp_node is self.head:
            self.head = self.head.next
        else:
            temp_node.previous.next = temp_node.next

        # Node is tail
        if temp_node is self.tail:
            self.tail = self.tail.previous
        else:
            temp_node.next.previous = temp_node.previous

    def find(self, data):
        temp_node = self.head

        while temp_node is not None:
            if temp_node.data is data:
                return temp_node

            temp_node = temp_node.next

        return temp_node

    def printListForward(self):
        temp_node = self.head

        while temp_node is not None:
            print temp_node.data
            temp_node = temp_node.next

    def printListBackward(self):
        temp_node = self.tail

        while temp_node is not None:
            print temp_node.data
            temp_node = temp_node.previous


DLL = DoubleLinkedList()

DLL.addToHead(1)
DLL.addToHead(2)
DLL.addToHead(3)

DLL.printListForward()

DLL.delete(2)

DLL.printListForward()