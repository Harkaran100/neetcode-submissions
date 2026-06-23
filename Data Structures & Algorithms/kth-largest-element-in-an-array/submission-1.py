class Solution:
    def findKthLargest(self,nums: list[int], k: int):
        # create minheap
        minHeap = []
        
        # iterate through array
        for i in nums:
            # push to array
            heapq.heappush(minHeap,i)
            # Keep at size k
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
        
        # to optimize can make it of size k everytime over pop something
        # once gone through entire array then can return minheap[0]
        # the only optimization this does is makes time n log k and space k instead of n