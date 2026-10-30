class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs: 
            hashMap = {} # letter count -> word
            for char in word:
                if char not in hashMap:
                    hashMap[char] = 0
                hashMap[char] += 1
            tMap = tuple(sorted(hashMap.items()))
            if tMap not in result:
                result[tMap] = []
            result[tMap].append(word)
        return list(result.values()) 

