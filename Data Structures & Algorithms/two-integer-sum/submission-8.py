class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                secondIndex = hashMap[target - nums[i]]
                return (list((secondIndex,i)))
            else:
                hashMap[nums[i]] = i
        