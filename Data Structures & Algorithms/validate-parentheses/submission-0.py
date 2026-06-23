class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")" : "(", "}" : "{", "]" : "["}
        for i in s:
            if i in mapping:  # closing bracket
                if stack and mapping[i] == stack[-1]: # closing bracket matches
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False

        
        