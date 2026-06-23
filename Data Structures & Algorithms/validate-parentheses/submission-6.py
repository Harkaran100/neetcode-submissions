class Solution:
    def isValid(self, s: str) -> bool:
        # we can use a stack here
        # since we know which finite strings can be in str
        # we can hardcode a map
        map = {"]":"[", ")": "(", "}": "{"}
        stack = []
        for char in s:
            if char in map.values():
                stack.append(char)
            else:
                if stack and stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        
