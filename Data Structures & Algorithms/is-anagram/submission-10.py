class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        if lenT != lenS:
            return False
        tMap = {}
        sMap = {}
        for char in s:
            if char not in sMap:
                sMap[char] = 0
            sMap[char] += 1
        
        for char in t:
            if char not in tMap:
                tMap[char] = 0
            tMap[char] += 1
        
        if tMap == sMap:
            return True
        return False
        