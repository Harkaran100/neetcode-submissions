class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input is array of strings
        # make keys the count of chars
        # make the value the strings
        # since only lower case letters
        # can we store in key as a count of the chars
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
            


        