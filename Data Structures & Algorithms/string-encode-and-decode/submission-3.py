class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for words in strs:
            length = len(words)
            res += (str(length) + "#" + words)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            currentNumLen = ""
            while s[i] != "#":
                currentNumLen += s[i]
                i += 1
            # now how to skip #
            i += 1
            currentCount = 0
            currentWord = ""
            while currentCount != int(currentNumLen):
                currentWord += s[i]
                currentCount += 1
                i += 1
            
            result.append(currentWord)
        return result
            

        # for all strs before a # add to currentNumLen
        # Once we hit a # add the next currentNumLen chars to a temporary holder which is then put into res


# count letters of word, add delimter and add to res string