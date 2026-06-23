# 1 is land 0 is water in a given 2d array
# count and return number of islads
# island is adjacent land masses vertical or horizontal
# can input be a null grid
# grid will have length 1 atleast
# only 1 and 0s are possible

# if see a 1

# for loop to go throiugh the 2d grid
# if see 0 continue
# if see 1 increment counter
# add to visited ! inside dfs
# call dfs on grid[r][c]
class Solution:
    def numIslands(self,grid: list[list[str]]):
        islandCount = 0
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            # out of bounds
            if (r < 0) or (c < 0) or (r >= rows) or (c >= cols):
                return
            # water
            if grid[r][c] == "0":
                return
            if (r,c) in visited:
                return
            visited.add((r,c))

            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)

        for r in range(rows):
            for c in range(cols):
                # water
                if grid[r][c] == "0":
                    continue
                if (r,c) in visited:
                    continue
                #land
                else:
                    islandCount += 1
                    dfs(r,c)
        return islandCount

