class KthLargest:
    def __init__(self,k:int,nums:list[int]):
        self.k = k
        self.minHeap = []
        # populate minHeap
        for num in nums:
            heapq.heappush(self.minHeap,num)
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
    def add(self,val: int):
        heapq.heappush(self.minHeap,val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]






