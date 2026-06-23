class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []


        def dfs(i, remaining):
            # base cases
            if remaining == 0:
                result.append(current.copy())
                return
            if remaining < 0:
                return
            if i == len(nums):
                return
        
            # case 1
            current.append(nums[i])
            dfs(i, remaining - nums[i])

            # case 2
            current.pop()
            dfs(i+1, remaining)

        dfs(0, target)
        return result

        
        #no repeating values
        # return all combinations add up to target in the list
        # can repeat values in a subset
        # can return in any order
        # once remaining == 0 copy subset into result

        # what is the core logic
        #[1,2] target = 6
        #[1,1,1,1,1,1]
        #[1,1,2,2]
        #[1,1,1,1,2]

        # 2 cases 
        # 2 - add the same number
        # 1 -  move onto the number

        # what are base cases
        #  - if remaining == 0 add to result
        # - if remaining < 0 dont add
        # - if i == len(nums) return

