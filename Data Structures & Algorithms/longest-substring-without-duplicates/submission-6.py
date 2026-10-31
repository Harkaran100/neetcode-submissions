class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # still use a set with left and right pointers
        # can solve i o of 1 space o of n time
        # keep incrementing right when no seen values, and calculate count and maxcount if hit repeated, move up left and remove its value frmo seen until return to valid set of chars then continue repeat until right < len(s)
        seen = set()
        maxCount = 0
        currCount = 0
        left = 0
        right = left

        if not s:
            return 0
        while right < len(s):
            char = s[right]
            if char not in seen:
                seen.add(char)
                currCount = (right - left) + 1
                maxCount = max(maxCount,currCount)
                right += 1
            else:
                while char in seen:
                    seen.remove(s[left])
                    left += 1
        return maxCount



        
        