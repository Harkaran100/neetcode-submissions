class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # made up of only lowercase english letters
        output = ""
        word1 = strs[0]
        print(word1)
        for letter in range(len(word1)):
            for word in strs:
                if len(word) <= letter or word1[letter] != word[letter]:
                    return output
            output += (word1[letter])
        return output


        
        
        
        
        
        
        
        # o of nxm sol 
        # for each letter in first word up til len of that word
        # get is first char go through all check until missing
        # return prefix


        # o of nx, sol
        # take the first entire word have that as "output" then mpve onto next word
        # see how many match, if only 2 match make output only what matches
        # now carry reduced prefix onto next
        # do this for all words

        