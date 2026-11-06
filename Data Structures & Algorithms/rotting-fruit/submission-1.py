class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # add all oranges to queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
        
        #traverse
        while queue:
            spread = False
            for i in range(len(queue)): # 1 bfs level / minute
                rotten = queue.popleft()
                for direction in directions:
                    r,c = direction
                    newRow, newCol  = rotten[0] + r, rotten[1] + c
                    if ((0 <= newRow < rows) and (0 <= newCol < cols)
                    and (grid[newRow][newCol] == 1)):
                        grid[newRow][newCol] = 2 # make it rotten
                        queue.append((newRow,newCol)) # add to queue
                        spread = True
            if spread:
                minutes += 1

        # check if any fresh fruit remain
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return minutes


        