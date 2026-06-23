class Solution:
    def isValid(self,s):
        matcher = {')': '(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i in matcher.values():
                stack.append(i)
            elif i in matcher:
                if not stack or stack[-1] != matcher[i]:
                    return False
                stack.pop()
            # i not in matcher at all
            else:
                return False
        return (len(stack) == 0)
            

        # it looks like a stack because of the order when looking at closing brackets
        # {[()]} stack = [] 
        # first step is to match the opening and closing brackets.
        # traverse s
        # if one of opening brackets is i, push into stack
        # if one of closing brackets is i, see if it matches with stack.peak()
        # if it matches do stack.pop() and increment i, if doesnt match return false
        # once reach end and if stack is empty return true
        #if not empty return false