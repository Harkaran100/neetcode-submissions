class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # need a map of prefix and postfix, do in two pass
        # when computing result multiply pre and post for that val
        prefix = []
        prefixProduct = 1
        postfix = []
        postfixProduct= 1
        result = []
        
        #prefix fill, need first val to be a 1
        for number in range(len(nums)):
            prefix.append(prefixProduct)
            prefixProduct *= nums[number]

        #postfix fill, last val needs to be a 1
        for number in reversed(range(len(nums))):
            postfix.append(postfixProduct)
            postfixProduct *= nums[number]

        postfix.reverse()
        # create result
        for i in range(len(nums)):
            answer = prefix[i] * postfix[i]
            result.append(answer)
        return result
            


