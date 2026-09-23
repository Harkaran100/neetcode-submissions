class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"}":"{", "]":'[', ")":"("}
        stack = []
        
        for i in s:
            if i in "([{":
                stack.append(i)
            elif stack and brackets[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        if stack:
            return False
        return True
    

        # if open / value append
        # elif close / key pop
        # return stack

        

        