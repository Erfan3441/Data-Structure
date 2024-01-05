class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def delete(self, key):
        try:
            index = self.heap.index(key)
        except ValueError:
            return False  # The key is not in the heap
        # If the element to be deleted is the last one, no need to bubble down
        if index == len(self.heap) - 1:
            self.heap.pop()
        else:
            # Move the last element to the place of the one to delete and bubble down or up as appropriate
            self.heap[index] = self.heap.pop()
            parent = self._parent(index)
            if index > 0 and self.heap[index] < self.heap[parent]:
                self._bubble_up(index)
            else:
                self._bubble_down(index)
        return True

    def search(self, key):
        try:
            self.heap.index(key)
            return True
        except ValueError:
            return False

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _bubble_up(self, index):
        parent = self._parent(index)
        if index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _bubble_down(self, index):
        smallest = index
        left_child = self._left_child(index)
        right_child = self._right_child(index)
        
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        
        if smallest != index:
            self._swap(index, smallest)
            self._bubble_down(smallest)


# min_heap = MinHeap()
# min_heap.insert(3)
# min_heap.insert(10)
# min_heap.insert(5)
# min_heap.insert(6)
# min_heap.insert(2)

# print("Heap before deletion:", min_heap.heap)
# min_heap.delete(10)
# print("Heap after deletion of 10:", min_heap.heap)
# print("Search for 5, should return True:", min_heap.search(5))
# print("Search for 10, should return False:", min_heap.search(10))