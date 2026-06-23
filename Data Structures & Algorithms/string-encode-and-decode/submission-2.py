class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "" # append all to this
        for word in strs:
            length = len(word)
            encoded_string += str(length) + "#" + word
        return encoded_string


    def decode(self, s: str) -> List[str]:
        # use two pointers 
        # first find out what the number of chars is in first word.
        result = []
        i = 0
        while len(s) > i:
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j]) # have length of current word
            result.append(s[j+1: j + 1 + length])
            i = j + 1 + length # resets i to after the word
        return result



# encode should make a list of strs into a single str

#decode should make a single str into original list of str

# to encode we need to use some sort of delimiter

# every valid ascii value can exist, makes the delimter hard to find.

# encoding is easy part, it is the decode that makes it somewhat difficult

# inital i was thinking of add delimiter at the end of each string.

# at start of each list add a number representing the number of chars in current str
# after that have a #, logic defines make the next x(number before # delimiter) a word, after that many letters are looked at, continue again
# after current check only 2 things should be possible another number which would indicate the len of next word, or nothing indication of end of encoded_string
# this is decode logic
# for encode logic simply count the len of each word add number to front and # and then do this to join all into a str
# time complexity for encode would be o(n) where n is all chars in all strs, space complexit would be 0(n) aswell where n is chars
# for decode it is o(n) time complexity to traverse encoded_string and space complexity is o(k) k is words