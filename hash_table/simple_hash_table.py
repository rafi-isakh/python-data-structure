from hash_item import HashItem

class SimpleHashTable(object):
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
    
    def _hash(self, key):
        mult = 1
        hash_val = 0

        for ch in key:
            hash_val += mult * ord(ch)
            mult += 1
        
        return hash_val % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)

        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size
        
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
    
    def get(self, key):
        h = self._hash(key)
        
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                print(self.slots[h].value)
                return self.slots[h].value
            h = (h + 1) % self.size
        
        return None

    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        self.get(key)

ht = SimpleHashTable() 
ht["good"] = "eggs" 
ht["better"] = "ham" 

for word in ("good", "better"): 
    v = ht[word] 
    print(v) 

print("The number of elements is: {}".format(ht.count)) 