class KthLargest:
    def __init__(self,k:int,nums:list[int]):
        self.k = k
        self.nums = nums
        self.minHeap = []
        # populate minHeap
        for i in self.nums:
            heapq.heappush(self.minHeap,i)
    def add(self,val: int):
        heapq.heappush(self.minHeap,val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]






