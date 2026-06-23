class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # iterate through both at once until reach end of t
        # if they match increment  i in s by 1 else just move t
        # when reach end of s and try to go forward return True
        # else at end return false
        sIndex = 0

        if len(s) == 0:
            return True
        for char in range(len(t)):
            # see if index matches
            if s[sIndex] == t[char]:
                sIndex += 1
            if sIndex == len(s):
                return True
        return False

            
