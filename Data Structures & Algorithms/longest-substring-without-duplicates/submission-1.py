class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubString = 0
        left = 0
        right = 0
        hashset = set()
        while right < len(s):
            if s[right] not in hashset:
                hashset.add(s[right])
                right += 1 # increment right pointer
            else: # duplicate came up
                hashset.discard(s[left])
                left +=1 # increment left pointer
            currentSubString = right - left
            longestSubString = max(longestSubString, currentSubString)
        return longestSubString

        