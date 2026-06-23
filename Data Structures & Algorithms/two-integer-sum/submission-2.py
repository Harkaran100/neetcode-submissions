class Solution:
    def twoSum(self, nums: List[int], target: int):
        hashmap = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in hashmap:
                return [hashmap[need],i]
            hashmap[x] = i
            