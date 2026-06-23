class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # find cells from which water can flow into both oceans
        # meaning if water is to start from here has to go to 
        # either (left or top bound) and (right or bottom)

        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(row,col, oceanSet, PrevHeight):
            # out of bounds
            if (row < 0) or (row >= rows) or (col < 0) or (col >= cols):
                return
            # height issue
            if heights[row][col] < PrevHeight:
                return
            if (row,col) in oceanSet:
                return
            oceanSet.add((row,col))

            dfs(row + 1, col, oceanSet, heights[row][col])
            dfs(row - 1, col, oceanSet, heights[row][col])
            dfs(row, col + 1, oceanSet, heights[row][col])
            dfs(row, col - 1, oceanSet, heights[row][col])

        
        # for loop for north and south
        for c in range(cols):
            dfs(0,c, pacific, heights[0][c])
            dfs(rows -1,c, atlantic, heights[rows - 1][c])
        
        # for loop for north and south
        for r in range(rows):
            dfs(r,0, pacific, heights[r][0])
            dfs(r,cols-1, atlantic, heights[r][cols -1])
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    result.append((r,c))
        return result