class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        i = 0
        while i < len(s):
            if (i + 1 < len(s)) and hashMap[s[i]] < hashMap[s[i+1]]:
                result += hashMap[s[i+1]] - hashMap[s[i]]
                i += 2
            else:
                result += hashMap[s[i]]
                i += 1
        return result