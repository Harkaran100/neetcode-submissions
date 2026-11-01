class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        seenLand = set() # put index

        def bfs(row,col):
            queue = deque()
            queue.append((row,col))
            seenLand.add((row,col))
            while queue:
                row, col = queue.popleft()
                # check directions
                # right boundary
                if col + 1 <= (len(grid[0]) -1) and grid[row][col + 1] == "1" and (row,col+1) not in seenLand:
                    seenLand.add((row, col + 1))
                    queue.append((row,col + 1))
                # left boundary
                if col - 1 >= 0 and grid[row][col - 1] == "1" and (row,col- 1) not in seenLand:
                    seenLand.add((row, col - 1))
                    queue.append((row,col - 1))
                # upper boundary
                if row + 1 <= (len(grid) - 1) and grid[row + 1][col] == "1" and (row + 1,col) not in seenLand:
                    seenLand.add((row + 1, col))
                    queue.append((row + 1,col))
                # lower boundary
                if row - 1 >= 0  and grid[row - 1][col] == "1" and (row -1 ,col) not in seenLand:
                    seenLand.add((row -1 , col))
                    queue.append((row - 1,col))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and ((row,col)) not in seenLand:
                    numIslands += 1
                    bfs(row,col)
        return numIslands

        
                
                
                

# 2d input
# grid[0] is row  grid[1] is col
# input grid
# edge of grid is water/ boundary
# iterate through when find a 1 check all surronding can do dfs or bfs
# if we find a 1 add that index to seen, each time we start this loop of finding 1 increment islands and when done move onto next element where is 1 and not in seen hashmap
# to account for out of bounds, we can say somehing like if out of bounds = 0
# onec gone through entire 2d array return num of islands