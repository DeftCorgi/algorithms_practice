class MaxHeap:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        self.heapifyUp()

    def peek(self):
        if not self.items:
            raise Exception("Empty Heap")
        return self.items[0]

    def poll(self):
        self.heapifyDown()
        return self.items.pop()

    def heapifyDown(self):
        current = 0
        self.swap(current, len(self.items)-1)
        while(self.hasLeft(current)):
            print('hasleft')
            left = self.getLeft(current)
            if (self.hasRight(current)):
                right = self.getRight(current)
                if left > right:
                    childIdx = self.getLeftIdx(current)
                else:
                    childIdx = self.getRightIdx(current)
            else:  # just has left child
                childIdx = self.getLeftIdx(current)

            self.swap(current, childIdx)
            current = childIdx

    def heapifyUp(self):
        "maintain heap property by bubbling up"
        current = len(self.items) - 1
        item = self.items[current]
        while current != 0 and item > self.getParent(current):
            parentIdx = self.getParentIdx(current)
            self.swap(current, parentIdx)
            current = parentIdx

    def swap(self, a, b):
        "swaps 2 items in array"
        temp = self.items[b]
        self.items[b] = self.items[a]
        self.items[a] = temp

    def hasParent(self, index): return True if self.getParent(index) else False

    def getParent(self, index): return self.items[(index - 1) // 2]

    def getParentIdx(self, index): return (index - 1) // 2

    def getLeft(self, index): return self.items[(index * 2) + 1]

    def getLeftIdx(self, index): return (index * 2) + 1

    def hasLeft(self, index): return True if self.getLeftIdx(
        index) < len(self.items) else False

    def getRight(self, index): return self.items[(index * 2) + 1]

    def getRightIdx(self, index): return (index * 2) + 1

    def hasRight(self, index): return True if self.getRightIdx(
        index) < len(self.items) else False

    def print(self):
        for i in range(len(self.items)):
            print(i, self.items[i])


heap = MaxHeap()
heap.push(5)
heap.push(6)
heap.push(3)
heap.poll()
heap.poll()
heap.print()
