class Solution:
    def isPalindrome(self, s: str) -> bool:
        # can use 2 pointers
        # only look at alphanumeric characters
        # ignore others
        # can be empty
        left = 0
        right = len(s) -1
        # how to only check alphanumeric
        # can be upper and lower, so i should lower all chars
        while left < right:
            while left < right and not s[left].isalnum(): # skip non alphanumeric
                left += 1
            while left < right and not s[right].isalnum(): # skip non alphanumeric
                right -= 1
            # compare
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -=1
        return True