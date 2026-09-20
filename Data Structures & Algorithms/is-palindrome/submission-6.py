class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphastr = ""
        for char in s:
            if char.isalnum():
                alphastr += char.lower()
         # return alphastr
        reverse = (alphastr[::-1])
        return alphastr == reverse
