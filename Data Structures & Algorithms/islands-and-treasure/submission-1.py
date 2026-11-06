class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0: # append all chests
                    queue.append((row,col))
        while queue: # traverse as much as possible
            index = queue.popleft()
            for direction in directions:
                r,c = direction
                newRow, newCol = index[0] + r, index[1] + c
                if ((0 <= newRow < rows) and (0<= newCol < cols)
                and (grid[newRow][newCol] == 2147483647)): 
                    grid[newRow][newCol] = grid[index[0]][index[1]] + 1
                    queue.append((newRow,newCol))
        return None

        # do bfs from all starting at once
        # no seen set needed, only travesrse if not inf and not 0

        # while queue do queue.pop append all of its correct vals, before appending put its new distance value?
        