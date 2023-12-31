from functools import total_ordering
from typing import TypeVar, Generic, List, Optional
import heapq

T = TypeVar('T')


@total_ordering
class MaxHeapWrapper(Generic[T]):
    def __init__(self, val: T) -> None:
        self.val = val

    def __lt__(self, other) -> bool:
        return self.val > other.val

    def __eq__(self, other) -> bool:
        return self.val == other.val

    def __repr__(self) -> str:
        return str(self.val)


class MaxHeap(Generic[T]):

    def __init__(self, val: Optional[List[T]] = None) -> None:
        if val is not None:
            self.heap: List[MaxHeapWrapper[T]] = list(map(lambda item: MaxHeapWrapper[T](item), val))
            heapq.heapify(self.heap)
        else:
            self.heap = []

    def push(self, val: T) -> None:
        heapq.heappush(self.heap, MaxHeapWrapper[T](val))

    def pop(self) -> T:
        return heapq.heappop(self.heap).val

    def empty(self):
        return len(self.heap) == 0

    def size(self) -> int:
        return len(self.heap)

    def top(self) -> T:
        return self.heap[0].val

    def heapsort(self) -> List[T]:

        result = [self.pop() for i in range(len(self.heap))]
        result.reverse()
        return result
