class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-i for i in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            larger = -heapq.heappop(maxheap)
            smaller = -heapq.heappop(maxheap)
            if larger - smaller > 0:
                heapq.heappush(maxheap, -(larger-smaller))
        if len(maxheap) == 1:
            return -maxheap[0]
        if not maxheap:
            return 0