class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        element = Node(data)
        
        if self.top:
            element.next = self.top
            self.top = element
        else:
            self.top = element

        self.size += 1
    
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            
            return data
        else:
            return None
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
