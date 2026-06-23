class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge case
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set() # to add visited indexes
        islandCount = 0

        def dfs(row, col):
            #out of bounds
            if (row < 0) or (row >= rows) or (col < 0) or (col >= cols):
                return
            # visited
            if (row,col) in visited:
                return
            #water
            if grid[row][col] == "0":
                return

            # add to visited
            visited.add((row,col))

            # continue dfs in all directions

            #right
            dfs(row, col + 1)
            #left
            dfs(row, col - 1)
            #up
            dfs(row -1, col)
            #down
            dfs(row + 1, col)
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1": # ensure not yet visited and land
                    islandCount += 1
                    dfs(r,c)
        return islandCount
        
        
        # traverse from [r][c]
        # first a row at a time by moving cols only and then go to the next col
        # when we hit a 1 check if in visisted hashset in hashset store the index of [row][col]
        # if not add to visited and += 1 to our global count
        # run dfs on it to check all connected paths,
        # each time we see a one add to visisted
        # once all visited continue with out travesal
        # check if visistd if not visit if it is continue
        # once at end return count
        