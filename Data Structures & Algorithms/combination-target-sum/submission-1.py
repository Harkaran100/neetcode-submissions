class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # array num has. disitinct ints, target int is target
        #return a list of all subset of distinct chars that sum to target
        # we can choose the same number several time
        # two combinations are the same if have same frequency of all chosen numbers
        # since we can even use the same number several times
        # i am thinking of posibly back tracking
        # try current index all if we go over target backtrack 1 and move on.
        # do this for entire i and then move i forward
        # what should backtrack function take as input? proabaly current list and its sum?
        result = []
        current = []
        def backTrack(start,currentNum):
            # base case
            if currentNum == target:
                result.append(current.copy())
                return
            # greater then target
            elif currentNum > target:
                return
            else:
                # less then target
                for i in range(start, len(nums)):
                    current.append(nums[i])
                    backTrack(i,currentNum + nums[i])
                    current.pop()
                

        backTrack(0,0)
        return result
        