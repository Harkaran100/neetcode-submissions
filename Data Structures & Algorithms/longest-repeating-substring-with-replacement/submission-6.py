class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {} # char -> count
        left = 0
        maxFreq = 0
        right = left
        maxCount = 0
        while right < len(s):
            char = s[right]
            if char not in freqMap:
                freqMap[char] = 0

            freqMap[char] += 1
            maxFreq = max(freqMap.values())
            if ((right - left) + 1) <= maxFreq + k:
                currCount = (right - left) + 1
                maxCount = max(maxCount,currCount)
                right += 1
            else:
                while ((right - left) + 1) > maxFreq + k:# remove left from freqMap and increment
                    freqMap[s[left]] -= 1
                    left += 1
                    maxFreq = max(freqMap.values())
                right += 1
        return maxCount
            
        