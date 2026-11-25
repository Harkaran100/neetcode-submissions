class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        # iterate through annd find 1s and run dfs or bfs
        # everytimr we start incremenet island
        # add all 1s to seen, so not to raverse same land
        land = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # check if 1 and not in seen
                if grid[row][col] == "1" and (row,col) not in land:
                    islands += 1
                    print(row,col)
                    queue = deque()
                    queue.append((row,col))
                    land.add((row,col))
                    while queue:
                        curVal = queue.popleft()
                        curRow, curCol = curVal[0], curVal[1]
                        #up
                        if int(curRow -1) >= 0 and (grid[curRow - 1][curCol] == "1") and (curRow - 1,curCol) not in land:
                            queue.append((curRow - 1,curCol))
                            land.add((curRow - 1,curCol))
                        #down
                        if int(curRow +1) < len(grid) and (grid[curRow + 1][curCol] == "1") and (curRow + 1,curCol) not in land:
                            queue.append((curRow + 1,curCol))
                            land.add((curRow + 1,curCol))
                        #left
                        if int(curCol - 1) >= 0 and (grid[curRow][curCol - 1] == "1") and (curRow,curCol - 1) not in land:
                            queue.append((curRow,curCol - 1))
                            land.add((curRow,curCol - 1))
                        #right
                        if int(curCol + 1) < len(grid[0]) and (grid[curRow][curCol + 1] == "1") and (curRow,curCol + 1) not in land:
                            queue.append((curRow,curCol + 1))
                            land.add((curRow,curCol + 1))
        return islands


                        
