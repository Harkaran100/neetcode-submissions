class Solution:
    def longestPalindrome(self, s: str) -> str:
        # check all combinations store longest in res
        # if find longer replace
        # use 2 pointers but how and where to start
        # left only moves with for loop right comes in until right = left
        
        longest = ""
        for left in range(len(s)):
            for right in range(left, len(s)):
                subString = s[left:right + 1]

                if subString == subString[::-1]:
                    if len(subString) > len(longest):
                        longest = subString
        return longest