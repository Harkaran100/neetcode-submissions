class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # val -> index
        for i in range(len(nums)): # iterate with index
            secondNum = target - nums[i]
            if hashMap and secondNum in hashMap:
                return ([hashMap[secondNum],i])
            hashMap[nums[i]] = i
        