class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            maxHeap.append(- stone)

        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if ((x + y) < 0):
                heapq.heappush(maxHeap, x-y)
        if maxHeap:
            return -(maxHeap[0])
        return 0


        