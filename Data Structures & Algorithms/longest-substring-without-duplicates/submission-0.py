class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hashmap = set()
        result = 0
        currentMax = 0
        while r < len(s):
            if s[r] not in hashmap:
                hashmap.add(s[r])
                r += 1
                currentMax = r - l
                result = max(result, currentMax)
            else:
                hashmap.remove(s[l])
                l+=1
        return result