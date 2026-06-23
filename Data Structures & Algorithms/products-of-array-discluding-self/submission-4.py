class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use two pointers
        # use prefix and postfix
        # for each index multipy its postfix and prefix
        # how to calculate prefix and post fix.
        # maybe in 2 passes?
        # pass one from left to right, before first multiplication base should be 1
        # maybe store prefix in a new list
        #.  [1,2,4,6].  prefix = [1,1,2,8] postfix = [48,24,6,1]
        # first pass for prefix second for postfix third to get answer by multiplying
        
        # first pass
        prefix = []
        prefix_count = 1
        for i in nums: #create prefix  list
            prefix.append(prefix_count)
            prefix_count *= i

        # second pass
        postfix = []
        postfix_count = 1
        for i in reversed(nums):
            postfix.append(postfix_count)
            postfix_count *= i
        postfix_reverse = postfix[::-1]

        # third pass get answer
        result = []
        for i in range(len(nums)):
            value = prefix[i] * postfix_reverse[i]
            result.append(value)
        return result