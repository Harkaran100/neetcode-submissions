class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window 
        # keep a hashMap of vals
        maxchars = 0
        left = 0
        right = 0
        hashMap = {}
        curr = 0
        while right < len(s):
            if s[right] not in hashMap:
                curr += 1
                maxchars = max(maxchars,curr)

                # add to hashMap
                hashMap[s[right]] = 1
                right += 1
            else:
                while s[right] in hashMap:
                    del hashMap[s[left]]
                    left += 1
                    curr -= 1
        return maxchars
        



        