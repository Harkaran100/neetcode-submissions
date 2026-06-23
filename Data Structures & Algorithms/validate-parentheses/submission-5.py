class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {")":"(", "]":"[", "}":"{" }
        stack = []
        for i in s:
            if i in hashMap.values():
                stack.append(i)
            elif not stack or hashMap[i] != stack[-1]:
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True
        #hashmap to make open bracket = close bracket
        # stack
        #)]}{[(
        # while i less then (len(s))
        # stack.append all opening brackets
        #if not opening bracket
        # (means its closing)check if closing bracket corresponds to stack.pop from hashmap
