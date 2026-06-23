class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram is words which have same letters
        # made up of lowercase english letters
        # there are 26 letters we can get in ascii 
        # store in hashmap key value pair
        # key is the list of asci for a word
        # value is the original word
        # at end return values

        hashmap = {}
        for word in strs:
            # how to store asci in a list?
            # since lowercase letters are in order starting at asci 62, we can do asci(i) - asci("a") that should give 0 index verision of it
            # can store in list like this
            key_list = [0] * 26
            for letter in word:
                # find a way to update correct ascii position in key_list
                position = ord(letter) - ord("a")
                key_list[position] += 1 # this should populate entire key_list
            key = tuple(key_list) # turn to tuple to use in hashmap
            if key not in hashmap:
                hashmap[key] = [] # this should be empty because the next line should add word
            hashmap[key].append(word) # add word
        return list(hashmap.values())