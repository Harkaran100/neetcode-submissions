class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # was in ascending order
        # now ahs been rotated between 1-n times
        # all elements are unique in nums

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1