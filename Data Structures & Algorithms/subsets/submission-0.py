class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result will be final thing I return
        result = []
        # Whilst traversing current will store a subset then append to res, current will be overwritten
        current = []

        # recursive function
        def dfs(i):
            # base case / copy into res
            if i == len(nums):
                result.append(current.copy())
                return

            #case 1 (include following i)
            current.append(nums[i])
            dfs(i+1)
            #case 2 (exclude following i)
            current.pop()
            dfs(i+1)
            
        dfs(0)
        # return at ending
        return result

        # Self notes
        # For backtracking recursion is needed, so i need to figure out how I can exit the recursion
        # via basecase and how I can move current to next subset and make sure no duplicates.

        
        