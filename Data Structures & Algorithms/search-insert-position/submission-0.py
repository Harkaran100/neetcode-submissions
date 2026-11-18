class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # brute force o of n time  o of 1 space
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target < nums[i]:
                return i
            else:
                continue
        # last index + 1
        return len(nums)
        