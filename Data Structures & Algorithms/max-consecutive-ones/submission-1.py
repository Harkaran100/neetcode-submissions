class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        maxCount = 0
        for right in range(len(nums)):
            if nums[right] == 0: # reset
                left = right + 1
            else:
                currCount = (right - left) + 1
                maxCount = max(maxCount,currCount)
        return maxCount


        
