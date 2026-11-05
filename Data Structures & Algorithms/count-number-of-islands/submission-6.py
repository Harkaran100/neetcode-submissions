class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        numIslands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row,col):
            seen.add((row,col))
            # right
            if row + 1 < rows and (row + 1,col) not in seen and grid[row+1][col] == "1":
                dfs(row+1,col)
            # left
            if row - 1 >= 0 and (row - 1,col) not in seen and grid[row-1][col] == "1":
                dfs(row-1,col)
            # up
            if col + 1 < cols and (row,col + 1) not in seen and grid[row][col + 1] == "1":
                dfs(row,col + 1)
            # down
            if col - 1 >= 0 and (row,col - 1) not in seen and grid[row][col - 1] == "1":
                dfs(row,col - 1)
            return


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in seen:
                    numIslands += 1
                    dfs(row,col)
        return numIslands