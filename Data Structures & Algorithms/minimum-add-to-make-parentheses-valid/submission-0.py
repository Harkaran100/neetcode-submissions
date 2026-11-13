class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openCount = 0
        additions = 0
        for bracket in range(len(s)):
            if s[bracket] == "(":
                openCount += 1
            else:
                if openCount > 0:
                    openCount -= 1
                else:
                    additions += 1
        return (additions + openCount)

