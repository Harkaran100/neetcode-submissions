class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for word in strs:
            charCount  = [0] * 26
            for letter in word:
                placement = ord(letter) - ord("a")
                charCount[placement] += 1
            charCountTup = tuple(charCount)
            if charCountTup not in hashMap:
                hashMap[charCountTup] = []
            hashMap[charCountTup].append(word)
        return list(hashMap.values())

        #time is  o of a where a is number of letters total in strs + o of n where n is total number of words (converting to tuple)
        # so overall time is o of n

        # space is of of c for charCount + o of u for hashmap where u is number of unique words.
        # overall space is o of n
