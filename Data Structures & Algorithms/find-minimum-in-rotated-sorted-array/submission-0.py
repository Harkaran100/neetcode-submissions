class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        while left < right:
            midpoint =  (left + right) // 2
            if nums[midpoint] > nums[right]: # rotation lies here
                left = midpoint + 1
            else: # rotation lies here
                right = midpoint
        return nums[left]