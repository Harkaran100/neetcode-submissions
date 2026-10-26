class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        maxLen = 0
        # helper
        def expand(left,right):
            nonlocal start, maxLen
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length = right - left + 1
                if length > maxLen:
                    start = left
                    maxLen = length
                left -= 1
                right += 1

        for char in range(len(s)):
            expand(char,char) #odd
            expand(char, char + 1) # even
        return s[start:start+maxLen]
