class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
        
        # can improve time complexity to log k instead of log n by doing a 
        # size k heap instead of size n
