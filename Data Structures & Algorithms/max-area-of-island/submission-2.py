class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        currIsland = 0

        # helper
        def dfs(row,col):
            nonlocal currIsland
            currIsland += 1
            seen.add((row,col))
            # right
            if (row + 1 < rows) and (row + 1,col) not in seen and grid[row + 1][col] == 1:
                dfs(row + 1, col)
            # left
            if (row - 1 >= 0) and (row - 1,col) not in seen and grid[row - 1][col] == 1:
                dfs(row - 1, col)
            # up
            if (col + 1 < cols) and (row,col + 1) not in seen and grid[row][col + 1] == 1:
                dfs(row, col + 1)
            # down
            if (col -1 >= 0) and (row ,col -  1) not in seen and grid[row][col - 1] == 1:
                dfs(row, col - 1)
            nonlocal maxIsland
            maxIsland = max(maxIsland, currIsland)


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in seen:
                    currIsland = 0
                    dfs(row,col)
        return maxIsland
        