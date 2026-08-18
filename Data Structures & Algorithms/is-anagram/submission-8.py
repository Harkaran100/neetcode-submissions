class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        # edge case
        if (len(s) != len(t)):
            return False
        # build sMap
        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = 0
            sMap[s[i]] += 1
        # build tMap
        for i in range(len(t)):
            if t[i] not in tMap:
                tMap[t[i]] = 0
            tMap[t[i]] += 1

        #compare
        if sMap == tMap:
            return True
        return False
        
#space is o of unique chars in s + unique chars in t
# time is o of s + t
        