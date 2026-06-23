class Solution:
    def isValid(self, s: str) -> bool:
        # create hardcoded dict of open and close
        openToClose = {"(":")","[":"]","{":"}" }

        # create stack
        stack = []
        for i in s:
            if i in openToClose.keys():
                stack.append(i)
            elif stack and i == openToClose[stack[-1]]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True