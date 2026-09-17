class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        
        if len(s) != len(t):
            return False
        
        for char in s:
            if char not in sMap:
                sMap[char] = 0
            sMap[char] += 1

        for char in t:
            if char not in tMap:
                tMap[char] = 0
            tMap[char] += 1
        if sMap == tMap:
            return True
        return False
        