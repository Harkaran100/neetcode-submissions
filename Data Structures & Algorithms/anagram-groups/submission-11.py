class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {} # -> hashMap - word, so hashMap in a hashmap 
        for word in strs:
            count = {}
            for letter in word:
                if letter not in count:
                    count[letter] = 0
                count[letter] += 1
            tCount = tuple(sorted(count.items()))
            
            if tCount not in hashMap:
                hashMap[tCount] = []
            hashMap[tCount].append(word)
        return list(hashMap.values())
            