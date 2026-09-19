class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for word in strs:
            anagramCalc = [0] * 26 # use ascii map
            for i in word:
                anagramCalc[ord(i) - ord("a")] += 1
            anagramCalcTuple = tuple(anagramCalc)
            if anagramCalcTuple not in hashMap:
                hashMap[anagramCalcTuple] = []
            hashMap[anagramCalcTuple].append(word)
        ans = hashMap.values()
        return list(ans)
        