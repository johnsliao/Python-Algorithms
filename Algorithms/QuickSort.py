

class QuickSort():
    def __init__(self):
        self.list = [5,1,4,2,3]

    def partition(self, list, size):
        if size < 2:
            return

        pivot = list[size-1]
        L, U = 0, size-1

        while L < U:

            while list[L] < pivot:
                L = L + 1
            while list[U] > pivot:
                U = U - 1

            print self.list, 'swap!'
            self.list[L], self.list[U] = self.list[U], self.list[L]
            print self.list

        self.partition(list, U)
        self.partition(list[L+1:], size-L-1)


    def quickSort(self):
        self.partition(self.list, len(self.list))

quickSort = QuickSort()
quickSort.quickSort()

print quickSort.list
