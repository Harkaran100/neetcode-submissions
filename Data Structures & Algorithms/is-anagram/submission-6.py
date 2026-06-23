class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        #build s hashmap
        for i in s:
            if i not in sMap:
                sMap[i] = 0
            sMap[i] += 1

        #build t hashmap
        for i in t:
            if i not in tMap:
                tMap[i] = 0
            tMap[i] += 1
        if sMap == tMap:
            return True
        return False



















        '''
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
        '''

        