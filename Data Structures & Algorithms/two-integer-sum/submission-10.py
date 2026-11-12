class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # val -> index
        for num in range(len(nums)):
            # check in num - target in hashmap
            secondNum = target - nums[num]
            if secondNum in hashMap:
                return [hashMap[secondNum],num]
            hashMap[nums[num]] = num
        
