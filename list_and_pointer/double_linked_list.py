class Node(object):
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1
    
    def delete(self, data):
        current = self.head
        node_deleted = False

        #if list empty
        if current is None:
            node_deleted = False
        elif current.data == data:
            # head will be deleted
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:
            # tail will be deleted
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current and not node_deleted:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted    = True
                current = current.next

        if node_deleted:
            self.count -= 1

    def size(self):
        return self.count
    
    def contain(self, data):
        for node_data in self.iter():
            if node_data == data:
                return True
        return False

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
