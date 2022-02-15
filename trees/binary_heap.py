#!/usr/bin/python


class BinaryHeap:
    """Minimum binary heap implementation"""

    def __init__(self):
        self._heap = []

    def insert(self, value):
        self._heap.append(value)
        if len(self._heap) > 1:
            idx = len(self._heap) - 1
            parent = (idx - 1) // 2
            if self._heap[parent] > value:
                print(f"Swapping {value}")
                self._perc_up(idx, parent)

    def insert_book(self, item):
        self._heap.append(item)
        self._perc_up_book(len(self._heap) - 1)

    def delete(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        value = self._heap.pop()
        self._perc_down(0)
        return value

    def heapify(self, not_a_heap):
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        while cur_idx >= 0:
            self._perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def _get_left(self, idx):
        return 2 * idx + 1

    def _get_right(self, idx):
        return 2 * idx + 2

    def _perc_up(self, idx, parent):
        if self._heap[parent] > self._heap[idx] and parent >= 0:
            print(f"Exchange {idx} with {parent}")
            self._heap[parent], self._heap[idx] = (self._heap[idx], self._heap[parent])
            self._perc_up(parent, (parent - 1) // 2)

    def _perc_down(self, cur_idx):
        while self._get_left(cur_idx) < len(self._heap):
            min_child_idx = self._get_min_child(cur_idx)
            if self._heap[cur_idx] > self._heap[min_child_idx]:
                self._heap[cur_idx], self._heap[min_child_idx] = (
                    self._heap[min_child_idx],
                    self._heap[cur_idx],
                )
            else:
                return
            cur_idx = min_child_idx

    def _get_min_child(self, parent_idx):
        if self._get_right(parent_idx) > len(self._heap) - 1:
            return self._get_left(parent_idx)
        right_child_idx = self._get_right(parent_idx)
        left_child_idx = self._get_left(parent_idx)
        if self._heap[right_child_idx] < self._heap[left_child_idx]:
            return right_child_idx
        return left_child_idx

    def _perc_up_book(self, cur_idx):
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],
                )
            cur_idx = parent_idx

    def __str__(self):
        return self._heap


if __name__ == "__main__":
    bh = BinaryHeap()
    bh.insert_book(5)
    bh.insert_book(3)
    bh.insert_book(9)
    bh.insert_book(1)
    print(bh._heap)

    print(bh.delete())
    print(f"After removing 1 -> {bh._heap}")

    print(bh.delete())

    print(f"After removing 3 -> {bh._heap}")
    print(bh._heap)

    bh2 = BinaryHeap()
    bh2.heapify([9, 7, 6, 1, 3])
    print(bh2._heap)
