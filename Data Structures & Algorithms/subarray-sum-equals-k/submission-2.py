class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix = {
            0:1
        }
        runningVal = 0
        for num in nums:
            runningVal += num
            # check if valid subarray
            if runningVal - k in prefix:
                result += prefix[runningVal-k]
            # update prefix
            if runningVal not in prefix:
                prefix[runningVal] = 0
            prefix[runningVal] += 1
        return result


        

        