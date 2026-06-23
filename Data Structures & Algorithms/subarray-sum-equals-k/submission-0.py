class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
         # calculate prefix of all nums
        # store in hashmap with calculation as key value as count
        sumCount = {0:1}
        total = 0
        count = 0

        for i in range(len(nums)):
            total += nums[i] # prefix for i

            # check if ans
            if total - k in sumCount:
                count += sumCount[total - k] # add to count
            
            # add total to hashmap
            if total not in sumCount:
                sumCount[total] = 0
            sumCount[total] += 1
        
        return count
        