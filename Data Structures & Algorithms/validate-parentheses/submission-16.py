class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            "}":"{",
            ")":"(",
            "]":"[",
        }
        openBracket = ["(","[","{"]
        stack = []
        for string in s:
            if string in openBracket:
                stack.append(string)
            else: # in close to open
                if stack and closeToOpen[string] == stack[-1]:
                    stack.pop()
                else:
                    return False # invalid
        if stack:
            return False
        return True
        