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

        # Node is head
        elif self.head.data is data:
            print 'Node is head'
        # Node is tail
        elif self.tail.data is data:
            print 'Node is tail'
        # Node is neither head nor tail
        else:
            print 'Node is neither head nor tail'


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