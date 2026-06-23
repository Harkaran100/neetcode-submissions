class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        array = []
        for x,y in points:
           formula =  ((x*x) + (y*y))
           array.append((formula,[x,y]))
        maxHeap = [(-s, z) for s, z in array]
        heapq.heapify(maxHeap)
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        # return points
        return [points for (_, points) in maxHeap]
        
        