class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #init vars
        maxString = 0
        hashMap = {}
        left = 0
        right = 0

        while right < len(s):
            if s[right] not in hashMap:
                hashMap[s[right]] = 0
            hashMap[s[right]] += 1
            #check duplication
            if hashMap[s[right]] > 1:
                while hashMap[s[right]] > 1:
                    hashMap[s[left]] -= 1
                    left += 1
            # calculate current length
            currString = right - left + 1
            #Compare with max length
            maxString = max(maxString, currString)
            right += 1
        return maxString
        