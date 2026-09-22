class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        left = 0
        longestStr = 0

        for right in range(len(s)):
            # add right to hashMap
            if s[right] not in hashMap:
                hashMap[s[right]] = 0
            hashMap[s[right]] += 1

            # check if over capacity
            mostRepeated = max(hashMap.values())
            while (right - left + 1) > (mostRepeated + k): # maybe need to recalc
                hashMap[s[left]] -= 1
                left += 1
                mostRepeated = max(hashMap.values())
            longestStr = max(longestStr, right - left + 1)
        return longestStr
            



        # use hashMap, purpose to track which key currently has the most, we are interested in the value/ how many of that key

        # our hashMap can grow to size of that value + k

        # when we go over that we remove left from hashMap and increment left recompute calc and keep doing it until we are at max value + key

        

        