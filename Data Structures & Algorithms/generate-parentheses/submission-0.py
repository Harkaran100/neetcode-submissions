class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(curr,openB,closeB):
            # basecase
            if (openB == n) and (closeB == n):
                result.append(curr)
                return
            # 2 choices 
            if (openB != n) or (closeB != n):
                # 1. add )
                if openB < n:
                    dfs(curr + "(", openB + 1, closeB)
                if closeB < openB:
                    dfs(curr + ")",openB, closeB + 1)
            

        dfs("",0,0)
        return result  