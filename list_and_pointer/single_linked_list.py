from node import Node

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        # if self.tail == None:
        #     self.tail = node
        # else:
        #     current = self.tail
        #     while current.next:
        #         current = current.next

        #     current.next = node

        # optimized 
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node
        
        self.size += 1
    
    def size(self):
        return self.size

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.head
        prev = self.head

        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False
    
    def clear(self):
        self.head = None
        self.tail = None
