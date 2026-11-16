class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen = 0
        maxOpen = 0
        for char in s:
            if char == "(":
                minOpen += 1
                maxOpen += 1
            elif char == ")":
                minOpen -= 1
                maxOpen -= 1
            else:
                minOpen -= 1
                maxOpen += 1
            if maxOpen == -1:
                return False
            if minOpen == -1:
                minOpen = 0

        if minOpen <= 0 <= maxOpen:
            return True
        return False



