class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            prev = nums[0]
            if nums[i] < prev:
                return nums[i]
            prev = nums[i]
        return nums[0]