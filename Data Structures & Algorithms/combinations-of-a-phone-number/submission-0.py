class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if len(digits) == 0:
            return result
        
        # idea create static mapping
        numToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(i,currStr):
            # base case
            if len(currStr) == len(digits):
                result.append(currStr)
                return
            for c in numToChar[digits[i]]:
                backtrack(i + 1,currStr + c)
        
        backtrack(0,"")
        return result