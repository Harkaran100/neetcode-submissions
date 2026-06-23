class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False

        lengthS1 = len(s1)
        
        # create hashmaps
        hashs1 = {}
        hashs2 = {}

        # populate s1
        for char in s1:
            if char not in hashs1:
                hashs1[char] = 0
            hashs1[char] += 1
        
        # created fixed window
        for i in range(lengthS1):
            char = s2[i]
            if char not in hashs2:
                hashs2[char] = 0
            hashs2[char] += 1

        # check inital window
        if hashs1 == hashs2:
            return True

        # slide window
        for right in range(lengthS1, len(s2)):
            rightChar = s2[right]
            if rightChar not in hashs2:
                hashs2[rightChar] = 0
            hashs2[rightChar] += 1

            leftChar = s2[right - lengthS1]
            hashs2[leftChar] -= 1

            if hashs2[leftChar] == 0:
                del hashs2[leftChar]

            if hashs1 == hashs2:
                return True

        
        # outer return False (if return true not hit inside)
        return False
        
        
        # check if s1 is a permuatation of s2
        # all together
        # hashmap but how?
        # thinking of creating hashmap for all of s1
        # then getting len of s1
        # create a fixed size window in len of s1 in s2
        # keep a hashmap of that fized window in s2, constantly comapre 2 hashmaps are same
        # if they are return true if not by end of s2 return false 