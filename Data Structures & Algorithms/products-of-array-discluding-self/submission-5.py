class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        result = []
        zeroCount = 0
        for i in nums:
            if i == 0:
                zeroCount += 1
            else:
                totalProduct *= i
        for i in nums:
            if zeroCount > 1:
                result.append(0)
            elif zeroCount == 1:
                if i == 0:
                    result.append(totalProduct)
                else:
                    result.append(0)
            else:
                result.append(totalProduct // i)
        return result