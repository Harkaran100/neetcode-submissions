class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        rows = len(heights)
        cols = len(heights[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(row,col,currentVal,ocean):
            if (row,col) in ocean:
                return
            # add to set
            ocean.add((row,col))
            for direction in directions:
                r,c = direction
                if ((0 <= row + r < rows) and (0 <= col + c < cols) 
                and (heights[row + r][col + c] >= currentVal)):
                    dfs(row + r, col + c, heights[row + r][col + c],ocean)


        # pacific
        for c in range(cols): # top 
            if (0,c) not in pacific:
                dfs(0,c,heights[0][c],pacific)

        for r in range(rows): # left
            if (r,0) not in pacific:
                dfs(r,0,heights[r][0],pacific)

        # atlantic

        for c in range(cols): # bottom
            if (rows -1,c) not in atlantic:
                dfs(rows-1,c,heights[rows-1][c], atlantic)
        for r in range(rows):
            if (r,cols - 1) not in atlantic:
                dfs(r,cols-1,heights[r][cols -1],atlantic)
        
        both = pacific & atlantic
        result = []
        for row,col in both:
            result.append([row,col])
        return result





        # atc (check last row, and last val in each col)


        # start from the oceans work your way in while = or greater then prev
        # keep track of valeues that can be reached from each ocean
        # for those that can be reached from both oceans return those indecie pairs

        
        