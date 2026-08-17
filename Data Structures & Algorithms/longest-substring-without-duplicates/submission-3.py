class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        count = 0
        left, right = 0, 0
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = 0
            hashMap[s[i]] += 1
            count += 1
            right += 1

            # check duplicate
            while hashMap[s[i]] == 2:
                hashMap[s[left]] -= 1
                count -= 1
                left += 1
            maxLen = max(count,maxLen)
        return maxLen

        # time is o of n
        # space is o of l where l is len of longest substring 