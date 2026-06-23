class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totallength = len(nums)
        result = [1] * totallength
        prefix = 1
        for i in range(totallength):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(totallength -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result