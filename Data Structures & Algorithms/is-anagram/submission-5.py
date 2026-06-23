class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count chars its o(n)
        if len(s) != len(t):
            return False
        # init hashmap
        hashmap = {}
        # build hashmap
        for i in s:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] +=1
        # unbuild hashmap
        for i in t:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] -= 1
        # check hashmap
        for value in hashmap.values():
            if value != 0:
                return False
        return True

        