class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #have 2 vars max length and current length
        maxLen = 0
        currentLen = 0
        # maintain hashset with current substring
        hashset = set()

        # init left pointer only right moves along
        left = 0
        for right in range(len(s)):
            
            # 2 cases
            # 1: next str repeat (move left + 1 and remove left value from hashset)
            while s[right] in hashset:
                hashset.discard(s[left])
                currentLen -= 1
                left += 1
                # dont need to recalculate currentLen
            # 2: next str new (only move right and add to hashset)
            if s[right] not in hashset:
                hashset.add(s[right])
                currentLen += 1
                maxLen = max(maxLen, currentLen)

        return maxLen
            # need to update currentLen counter


        