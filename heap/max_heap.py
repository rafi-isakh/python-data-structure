class MaxHeap(object):
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

    def max_index(self, index):
        if index*2 + 1 > self.size:
            return index*2
        elif self.heap[index*2] > self.heap[index*2+1]:
            return index*2
        else:
            return index*2 + 1

    def floating(self, index):
        while index // 2 > 0:
            if self.heap[index] > self.heap[index//2]:
                self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
            
            index //= 2
    
    def sinking(self, index):
        while index*2 <= self.size:
            next_index = self.max_index(index)
            if self.heap[index] < self.heap[next_index]:
                self.heap[index], self.heap[next_index] = self.heap[next_index], self.heap[index]
            
            index = next_index


h = MaxHeap() 
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6): 
    h.insert(i)

for i in range(10): 
    n = h.pop() 
    print(n)