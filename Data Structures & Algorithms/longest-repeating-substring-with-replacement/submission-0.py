class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # hashmap
        l = 0
        maxResult = 0 # max
        currentMax = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l +=1
            currentMax = r - l + 1
            maxResult = max(maxResult, currentMax)
        return maxResult
        # use sliding window to find current max
        # on second pass check that many k ints to left or right and add