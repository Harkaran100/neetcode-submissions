class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numberofZeros = 0
        product = 1
        result = []
        for i in nums:
            if i == 0:
                numberofZeros += 1
            else:
                product *= i
        # all zeros
        if numberofZeros > 1:
            result0 = [0] * len(nums)
            return result0
        elif numberofZeros == 1:
            for i in nums:
                if i != 0:
                    result.append(0)
                else:
                    result.append(product)
            return result

        else:
            for i in nums:
                result.append(product // i)
            return result