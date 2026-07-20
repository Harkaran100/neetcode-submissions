class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in numsMap:
                return [numsMap[value],i] 
            numsMap[nums[i]] = i

        
        