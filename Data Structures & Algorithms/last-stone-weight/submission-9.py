class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # val repersents weight of ith index
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) > 1:
            stone1 = -(heapq.heappop(maxHeap))
            stone2 = -(heapq.heappop(maxHeap))
            newStone = stone1 - stone2
            if newStone > 0:
                heapq.heappush(maxHeap,-newStone)
        if maxHeap:
            return -maxHeap[0]
        return 0
            