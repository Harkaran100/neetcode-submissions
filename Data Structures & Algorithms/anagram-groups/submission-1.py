class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for word in strs:
            temporary = [0] * 26
            for char in word:
                temporary[ord(char) - ord("a")] += 1
                # we are populate hashmap with correct keys
            key = tuple(temporary)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        return list(hashmap.values())



        # hashmap??
        # can only include lowercase english letters 26 possible options, ascii values??
        # key and value pair
        # use ascii somehow
        