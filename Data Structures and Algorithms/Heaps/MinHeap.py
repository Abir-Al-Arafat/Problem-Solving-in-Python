class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

minheap = MinHeap()
# [95, 75, 80, 55, 60, 50, 65]
minheap.insert(95)
minheap.insert(75)
minheap.insert(80)
minheap.insert(55)
minheap.insert(60)
minheap.insert(50)
minheap.insert(65)
print(minheap.heap)