class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # look in hashmap for second value
        hashmap = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in hashmap:
                return [hashmap[value],i]
            hashmap[nums[i]] = i