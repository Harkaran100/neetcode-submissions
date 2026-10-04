import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxHeap = []
        result = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(maxHeap,[-distance,point])
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        while maxHeap:
            coordinate = heapq.heappop(maxHeap)
            result.append(coordinate[1])
        return result

        # calculate eucdilan distance store as key and val as the points
        # use minheap and pop vals and append the val to res for the first k points

        # maxheap  5,4,3,2,1
        # minheap 1,2,3,4,5
        # k = 2

        # return associated value
        # can use minheap and count var when count = k stop popping and resturn res (if popping to res)
        # space complexity would be o of n where we put all points and eucdilan in heap
        # or use maxheap and keep at size k if grows pop out 
        # more space/ memory efficent at o of k