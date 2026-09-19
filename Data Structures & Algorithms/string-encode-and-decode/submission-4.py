class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            length = len(word)
            result += (str(length) + "#" + word)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        number = ""
        char = 0
        while char < (len(s)):
            if s[char] != "#":
                number += s[char]
                char += 1
            else:
                wordLen = int(number)
                # the word is 1 char after now + wordlen
                result.append(s[char + 1: char + 1 + wordLen])
                # reset
                number = ""
                # move char to after word
                char += wordLen + 1
        return result
