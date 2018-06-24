class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, item):
        hashValue = self._hash(key)
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = item
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = item
            else:
                nextSlot = self._rehash(hashValue)
                while self.slots[nextSlot] != None and self.slots[nextSlot] == key:
                    nextSlot = self._rehash(nextSlot)
                if self.slots[nextSlot] == key:
                    self.data[nextSlot] = item
                else:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = item

    def _hash(self, key):
        return key % self.size

    def _rehash(self, oldhash):
        return (oldhash + 1) % self.size


h = HashTable()

h.put(5, {'name': 'Toan'})
h.put(5, {'name': 'Ivy'})
h.put(6, {'name': 'Tina'})
h.put(7, {'name': 'Jenny'})
h.put(2, {'name': 'Julie'})

print(h.data)
