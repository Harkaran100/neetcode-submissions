class Solution:
    def isValid(self, s: str):
        #matching dict
        mapping = {")": "(" , "}" : "{" , "]" : "[" }
        stack = []
        for i in s:
            if i in mapping:
                if stack and mapping[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False