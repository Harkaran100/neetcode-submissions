class Solution:
    def twoSum(self, nums: List[int], target: int):
        checked = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in checked:
                return [checked[complement], i]
            checked[n] = i