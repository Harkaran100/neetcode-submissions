class Solution:
    def isValid(self, s: str) -> bool:
        # everytime open bracket apend
        # close bracket pop last if matching
        # else return false
        brackets = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if i in "([{": # open bracket
                stack.append(i)
            elif stack and brackets[i] == stack[-1]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True



        

        