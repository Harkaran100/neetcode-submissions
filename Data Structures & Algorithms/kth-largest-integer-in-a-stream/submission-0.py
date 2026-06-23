class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.kth = k

        heapq.heapify(self.minheap)
        while len(self.minheap) > self.kth:
            heapq.heappop(self.minheap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        # edge case if array less then k
        if len(self.minheap) > self.kth:
            heapq.heappop(self.minheap)
        return self.minheap[0]

      

