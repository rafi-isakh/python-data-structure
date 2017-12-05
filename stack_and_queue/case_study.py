from random import randint
import time
from stack import Stack
from queue import Queue

# Balance bracket checking
def check_brackets(statement):
    stack = Stack()

    for ch in statement:
        if ch in ('(', '{', '['):
            stack.push(ch)
        if ch in (')', '}', ']'):
            element = stack.pop()
        
            if element is '(' and ch is ')':
                continue
            elif element is '{' and ch is '}':
                continue
            elif element is '[' and ch is ']':
                continue
            else:
                return False

    if stack.size > 0:
        return False
    else:
        return True

# Media player queue
class Track:
    def __init__(self, title=None):
        self.title  = title
        self.length = randint(5, 10)

class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()
    
    def add_track(self, track):
        self.enqueue(track)
    
    def play(self):
        while self.count > 0:
            current_track = self.dequeue()  
            print('Now playing {}'.format(current_track.data.title))
            time.sleep(current_track.data.length)
