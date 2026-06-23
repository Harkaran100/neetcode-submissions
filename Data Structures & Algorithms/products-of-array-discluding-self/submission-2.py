class Solution:
    def productExceptSelf(self,nums: List[int]):
        # without div, I can create a prefix and a post fix
        # for each i multiply the prefix and postfix and return at its index
        # how?
        # example
        #[2,3,4,5] prefix -> [1,2,6,24] postfix -> [60,20,5,1]
        # how to use these?
        # answer should be [60,40,30,24] # checks out if we 
        # multiply that locations prefix and postfix
        # need 2 passes to create prefix and postfix
        # can do above in res to save space

        # initalize result
        res = [1] * len(nums)

        #calculate prefix
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        #calculate postfix
        postfix = 1
        for i in range(len(nums) -1, -1, -1): # do it backwords somehow
            res[i] *= postfix
            postfix *= nums[i]
        return res