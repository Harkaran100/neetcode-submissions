class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # take full first word as output decrement as I go
        output = strs[0]
        for word in strs:
            for letter in range(len(word)):
                if len(output) > letter and word[letter] == output[letter]:
                    continue
                else:
                    output = word[0:letter]
                    break # next word
            output = output[0:len(word)]
            if len(output) == 0:
                return ""
        return output

        