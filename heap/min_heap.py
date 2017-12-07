class MinHeap(object):
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.floating(self.size)

    def pop(self):
        value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1

        self.sinking(1)
        return value

    def min_index(self, index):
        if index*2 + 1 > self.size:
            return index*2
        elif self.heap[index*2] < self.heap[index*2+1]:
            return index*2
        else:
            return index*2 + 1

    def floating(self, index):
        while index // 2 > 0:
            # compare parent and children
            if self.heap[index] < self.heap[index//2]:
                self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
       
            # move up the tree
            index //= 2

    def sinking(self, index):
        while index*2 <= self.size:
            next_index = self.min_index(index)
            # compare parent and children
            if self.heap[index] > self.heap[next_index]:
                self.heap[index], self.heap[next_index] = self.heap[next_index], self.heap[index]
            
            # move down the tree
            index = next_index
