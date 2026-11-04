class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLen = 0
        currLen = 0
        charinSubstring = set()
        left = 0
        right = 0
        while right < (len(s)):
            if s[right] not in charinSubstring:
                charinSubstring.add(s[right])
                currLen += 1
                right += 1

                # compare with max
                longestLen = max(longestLen,currLen)
            else: # keep removing left and increment
                charinSubstring.remove(s[left])
                left += 1
                currLen -= 1
        return longestLen

        # currently 

        #