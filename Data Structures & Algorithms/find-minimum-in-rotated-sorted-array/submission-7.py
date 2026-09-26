class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        for i in nums:
            minimum = min(minimum, i)
        return minimum



        # sorted in ascending and all vals unique
        # return minimum element of this array
        