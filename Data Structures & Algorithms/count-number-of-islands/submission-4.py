class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        numIslands = 0

        def dfs(row,col):
            if row > (len(grid) -1)  or row < 0: # check row validity
                return False
            elif col > (len(grid[0]) -1) or col < 0: # check col validity
                return False
            elif grid[row][col] == "0" or (row,col) in seen: 
                return False
                
            if grid[row][col] == "1":
                seen.add((row,col)) # add to seen

            
            dfs(row + 1,col)
            dfs(row - 1,col)
            dfs(row ,col + 1)
            dfs(row ,col - 1)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in seen:    
                    numIslands +=1
                    dfs(row,col)
        return numIslands
        