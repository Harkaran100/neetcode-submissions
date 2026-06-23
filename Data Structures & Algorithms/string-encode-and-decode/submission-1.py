class Solution:
    def encode(self, words: list[str]):
        res = ""
        for i in words:
            res += str(len(i)) + "#" + i
        return res
    def decode(self, s: str):
        # a list
        res = []
        i = 0
        # so we dont go out of bounds
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            # start of the word
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
