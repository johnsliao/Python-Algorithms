class MinHeap():
    def __init__(self):
        self.data = []
        self.heapSize = 0

    def insert(self, data):
        self.data.append(data)
        self.heapSize += 1
        self.siftUp(self.heapSize-1)

    def deleteMin(self):
        if self.heapSize is 0:
            return

        self.data[0] = self.data[self.heapSize-1]
        self.heapSize -= 1
        self.siftDown(0)

    def siftDown(self, index):
        leftChild = self.getLeftChild(index)
        rightChild = self.getRightChild(index)

        if leftChild >= self.heapSize or rightChild >= self.heapSize:
            return

        if self.data[rightChild] < self.data[leftChild]:
            minIndex = rightChild
        else:
            minIndex = leftChild

        if self.data[index] > self.data[minIndex]:
            self.data[index], self.data[minIndex] = self.data[minIndex], self.data[index]
            self.siftDown(minIndex)

    def siftUp(self, index):
        if index is 0:
            return

        parentIndex = self.getParent(index)
        if self.data[index] < self.data[parentIndex]:
            self.data[index], self.data[parentIndex] = self.data[parentIndex], self.data[index]
            self.siftUp(parentIndex)

    def getLeftChild(self, index):
        return index * 2 + 1

    def getRightChild(self, index):
        return index * 2 + 2

    def getParent(self, index):
        return (index-1)/2

    def printHeap(self):
        for x in range(self.heapSize):
            print self.data[x]


minHeap = MinHeap()

minHeap.insert(10)
minHeap.insert(2)
minHeap.insert(3)
minHeap.insert(8)
minHeap.insert(12)
minHeap.insert(25)

minHeap.deleteMin()
minHeap.printHeap()