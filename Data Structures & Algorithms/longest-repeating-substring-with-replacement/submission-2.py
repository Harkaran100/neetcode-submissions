class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        left = 0
        maxRepeat = 0
        currRepeat = 0
        for right in range(len(s)):
            # add
            if s[right] not in hashMap:
                hashMap[s[right]] = 0
            hashMap[s[right]] += 1
            # check if valid
            currRepeat = max(hashMap.values())
            window = right - left + 1
            if window - currRepeat > k:
                hashMap[s[left]] -=1
                left += 1
            maxRepeat = max(maxRepeat,right - left + 1)
        return maxRepeat

