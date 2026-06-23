class Solution:
    def productExceptSelf(self,nums: List[int]):
        # this can be done by multiplying the prefix and postfix of index 
        # how to build prefix and post fix?
        # nums = [1,2,4,6]
        # prefix = [1,1,2,8] postfix = [48,24,6,1]
        # result = [1*48,1*24,2*6,8*1]
        # result = [48,24,12,8]

        # need to handle edge cases for 0
        # if 1 0 then what
        # if 2 zeros everything will be 0

        length = len(nums)
        result = [1] * length

        # set prefix and postfix
        prefix = 1
        postfix = 1

        # prefix
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        # postfix
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result

        