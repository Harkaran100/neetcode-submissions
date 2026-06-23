import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones] # negate all values (max heap work around)
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1: # 2 or more elements
            a = heapq.heappop(maxHeap)
            b = heapq.heappop(maxHeap)
            res = abs(a - b)
            if res == 0:
                continue
            else:
                heapq.heappush(maxHeap,-res)
        if maxHeap:
            return -(maxHeap[0])
        return 0
            # ex. -6 and -4
        # need to heapify stones
        # max heap
        # while len(1)
        # a = pop
        # b = pop
        # res = a-b
        # if res not 0 then push res to heap, remember to push as negative for minheap
        #
        