class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # iterate through, dont travrse same land twice (use a set)
        maxLand = 0
        seenLand = set()

        def dfs(row,col):
            # check out of bound
            if not(0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
                return 0
            # check if in seen
            if (row,col) in seenLand:
                return 0
            if grid[row][col] == 0:
                return 0
            
            seenLand.add((row,col))
            
            up = dfs(row-1,col)
            down = dfs(row+1,col)
            left = dfs(row,col-1)
            right = dfs(row,col+1)

            return (up + left + right + down + 1)



        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row,col) not in seenLand:
                    currLand = dfs(row,col)
                    maxLand = max(maxLand,currLand)
        return maxLand

        