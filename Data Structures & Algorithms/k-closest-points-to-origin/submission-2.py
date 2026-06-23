class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        # compute all eucaldian distance
        for i in points:
            distance = math.sqrt((i[0] - 0)**2 + (i[1] - 0)**2)
            minHeap.append((distance, i)) # build inital minHeap
        heapq.heapify(minHeap)

        result = [] # will return this
        while k > 0:
            result.append(heapq.heappop(minHeap)[1])
            k -= 1
        return result


        



        # push into minheap with (calculation,points)

        # while k not 0keep popping ad appending to res, but append just the list
        # after each time do k-=1