class Heap:

    def __init__(self, arr: list[int]) -> None:
        self.heap = arr

    def __str__(self):
        return f"{self.heap}"

    @staticmethod
    def get_left_right_child_index(i: int) -> tuple[int, int]:
        return (2 * i) + 1, (2 * i) + 2

    @staticmethod
    def get_parent_index(i: int) -> int:
        return (i - 1) // 2

    def is_leaf(self, i: int) -> bool:
        left_child_idx, _ = Heap.get_left_right_child_index(i)
        return left_child_idx >= len(self.heap)

    def _sift_down(self, idx: int) -> None:
        while not self.is_leaf(idx):
            left_idx, right_idx = Heap.get_left_right_child_index(idx)
            larger_child_idx = (
                right_idx if right_idx < len(self.heap) and self.heap[right_idx] > self.heap[left_idx] else left_idx
            )
            if self.heap[idx] >= self.heap[larger_child_idx]:
                break
            self.heap[larger_child_idx], self.heap[idx] = self.heap[idx], self.heap[larger_child_idx]
            idx = larger_child_idx

    def _sift_up(self, idx: int) -> None:
        while idx > 0:
            parent_idx = self.get_parent_index(idx)
            if self.heap[idx] <= self.heap[parent_idx]:
                break
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx

    def heapify(self) -> None:
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._sift_down(i)

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> int:
        if not self.heap:
            raise IndexError("pop from empty heap")
        top = self.heap[0]
        last = self.heap.pop()
        self._sift_down(0)
        if self.heap:  # false when the heap had exactly one element
            self.heap[0] = last
            self._sift_down(0)
        return top


heap1 = Heap([10, 20, 15, 12, 40, 25, 18])

heap1.heapify()
print(heap1)

heap1.insert(50)
print(heap1)

top = heap1.pop()
print(top)
print(heap1)
