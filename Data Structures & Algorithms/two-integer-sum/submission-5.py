class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            value1 = target - nums[i]
            if value1 in hashMap:
                return [hashMap[value1], i]
            else:
                hashMap[nums[i]] = i

        