class MaxHeap:
    def __init__(self):
        """
        Initialize an empty max-heap.
        """
        self.arr = []

    def insert(self, value):
        """
        Insert a new value into the max-heap.
        """
        self.arr.append(value)
        self._heapify_up(len(self.arr) - 1)

    def extract_max(self):
        """
        Remove and return the maximum value from the max-heap.
        """
        if len(self.arr) == 0:
            raise IndexError("extract_max from an empty heap")
        if len(self.arr) == 1:
            return self.arr.pop()
        root = self.arr[0]
        self.arr[0] = self.arr.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        """
        Maintain the heap property by moving the value at index up to its correct position.
        """
        parent_index = (index - 1) // 2
        if index > 0 and self.arr[index] > self.arr[parent_index]:
            self.arr[index], self.arr[parent_index] = self.arr[parent_index], self.arr[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """
        Maintain the heap property by moving the value at index down to its correct position.
        """
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if (left_child_index < len(self.arr) and self.arr[left_child_index] > self.arr[largest]):
            largest = left_child_index
        if (right_child_index < len(self.arr) and self.arr[right_child_index] > self.arr[largest]):
            largest = right_child_index

        if largest != index:
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            self._heapify_down(largest)

# Example usage
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
print(heap.extract_max())  # Outputs: 20
print(heap.extract_max())  # Outputs: 10
