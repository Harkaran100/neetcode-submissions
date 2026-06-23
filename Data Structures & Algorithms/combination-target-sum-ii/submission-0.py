class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current = []

        def dfs(i, remaining):
            #base cases
            if remaining == 0:
                result.append(current.copy())
                return
            if remaining < 0:
                return
            if len(candidates) == i:
                return

            # case 1
            current.append(candidates[i])
            dfs(i+1, remaining - candidates[i])
            current.pop()

            # case 2
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j+=1
            dfs(j, remaining)


        dfs(0,target)
        return result