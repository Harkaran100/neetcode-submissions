class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # given interger array can contain duplicates
        # can not reuse indexes or give duplicate sublists
        #return unique combos

        # can first sort

        candidates.sort()
        result = []
        current = []
        def backTrack(start,currentNum):
            # base case
            if currentNum == target:
                result.append(current.copy())
                return
            # over target
            elif currentNum > target:
                return
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    current.append(candidates[i])
                    backTrack(i + 1,currentNum +candidates[i])
                    current.pop()
        
        backTrack(0,0)
        return result