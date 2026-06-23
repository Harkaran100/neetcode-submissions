class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        currentMax = 0
        visited = set()

        def dfs(row,col):
            nonlocal currentMax
            # edge cases
            if (row < 0) or (row >= rows) or (col < 0) or (col >= cols):
                return
            elif (row,col) in visited:
                return
            elif grid[row][col] == 0:
                return
            else:
                visited.add((row,col))
                currentMax += 1

                dfs(row + 1,col) # up
                dfs(row - 1,col) # down
                dfs(row,col + 1) # right
                dfs(row,col - 1) # left

        for row in range(rows):
            for col in range(cols):
                # if water skip
                if grid[row][col] == 0:
                    continue
                else: # land
                    currentMax = 0
                    dfs(row,col)
                    # compare to max
                    maxArea = max(maxArea, currentMax)
        
    
        return maxArea



       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
"""
        #lengths of rows and cols
        rows = len(grid) # 4
        cols = len(grid[0]) # 5

        # track visited indcies
        visited = set()

        # max area tracker
        maxArea = 0

        def dfs(r,c):
            nonlocal currentArea
            # check out of bounds
            if (r < 0) or (r >= rows) or (c < 0) or (c >= cols):
                return
            # water
            elif grid[r][c] == 0:
                return
            # visited
            elif (r,c) in visited:
                return
            else:
                visited.add((r,c))
                currentArea += 1
            
            # recursion
            dfs(r + 1,c) # up
            dfs(r - 1,c) # down
            dfs(r,c + 1) # right
            dfs(r,c - 1) # left

        for r in range(rows):
            for c in range(cols):
                currentArea = 0
                # not visited and is land
                if (r,c) not in visited and grid[r][c] == 1:
                    dfs(r,c)
                    # compare with max
                    maxArea = max(maxArea, currentArea)
        return maxArea
        
        # traverse entire 2d array
        # check if not visited and index = 1
        # if so 
"""
        