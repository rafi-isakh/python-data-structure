class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        
        self.count += 1

    def dequeue(self):
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.count -= 1
            self.head = current.next
            self.head.prev = None
        
        return current
