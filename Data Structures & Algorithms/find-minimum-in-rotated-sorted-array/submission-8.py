class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        while left < right:
            midPoint = (left + right) // 2
            if nums[midPoint] > nums[right]:
                left = midPoint + 1
            else: 
                right = midPoint
        return nums[left]

    #[1,2] left/ mid = 1, right = 2


        # sorted in ascending and all vals unique
        # return minimum element of this array
        