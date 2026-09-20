class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        # track longest and current
        longestSequence = 1
        currentSequence = 1
        i = 0
        for i in range(1,len(nums)):
            if (nums[i]) == (nums[i-1 ] + 1):
                currentSequence += 1
                longestSequence = max(longestSequence, currentSequence)
            elif (nums[i]) == (nums[i-1]):
                continue
            else:
                currentSequence = 1
        return longestSequence
