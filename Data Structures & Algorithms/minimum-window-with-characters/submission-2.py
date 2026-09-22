class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tMap = {}
        sMap = {}
        left = 0
        minLength = 10**9

        #buildtMap
        for i in range(len(t)):
            if t[i] not in tMap:
                tMap[t[i]] = 0
            tMap[t[i]] += 1
        
        # chars in tMap
        need = len(tMap)
        have = 0

        # iterate through s
        for right in range(len(s)):
            if s[right] not in sMap:
                sMap[s[right]] = 0
            sMap[s[right]] += 1

            if s[right] in tMap and sMap[s[right]] == tMap[s[right]]: # same length
                have += 1
            while have == need: #here check for min
                currentLen = right - left + 1
                if currentLen < minLength:
                    minLength = currentLen
                    bestLeft = left
                    bestRight = right
                sMap[s[left]] -=1
                if s[left] in tMap and sMap[s[left]] < tMap[s[left]]:# != eql
                    have -= 1
                left += 1
        if minLength != 10**9:
            return s[bestLeft:bestRight+ 1]
        return ""


