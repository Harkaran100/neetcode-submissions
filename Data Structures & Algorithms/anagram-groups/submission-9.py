class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {} # count -> word
        for word in strs:
            count = [0] * 26
            for letter in word:
                asciiVal = ord(letter) - ord("a")
                count[asciiVal] += 1
            tCount = tuple(count)
            if tCount not in hashMap:
                hashMap[tCount] = []
            hashMap[tCount].append(word)
        return list(hashMap.values())