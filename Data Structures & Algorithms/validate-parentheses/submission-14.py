class Solution:
    def isValid(self, s: str) -> bool:
        # if open bracket always push
        # if close bracket see if last spot matches it and then if so pop else return False
        # at end check if s is empty
        openBracket = ["(","[","{"]
        stack = []
        closeToOpen = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        for i in s:
            if i in openBracket: # push openBrackets
                stack.append(i)
            elif i in closeToOpen:
                if stack and closeToOpen[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True


        

        