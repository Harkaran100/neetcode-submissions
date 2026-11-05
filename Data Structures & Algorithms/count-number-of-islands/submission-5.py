class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # can do dfs or bfs
        # both would be o of n time
        # bfs would use queue and be iterative we would also need a set for seen vals
        # bfs solution
        seen = set()
        numIslands = 0
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in seen:
                    print(queue.append((row,col)))
                    numIslands += 1
                    while queue:
                        node = queue.pop()
                        nodeRow, nodeCol = node
                        seen.add((nodeRow,nodeCol))
                        # add all others , for each check if in index, if 1 and  not in seen

                        # check up
                        if (nodeRow + 1 < len(grid)) and (grid[nodeRow + 1][nodeCol] == "1") and (nodeRow + 1,nodeCol) not in seen:
                            queue.append((nodeRow + 1,nodeCol))
                        # check down
                        if (nodeRow -1 >= 0) and (grid[nodeRow - 1][nodeCol] == "1") and (nodeRow - 1,nodeCol) not in seen:
                            queue.append((nodeRow -1,nodeCol))
                        # check left
                        if (nodeCol -1 >= 0) and (grid[nodeRow][nodeCol - 1] == "1") and (nodeRow,nodeCol - 1) not in seen:
                            queue.append((nodeRow,nodeCol - 1))
                        # check right
                        if (nodeCol + 1 < len(grid[0])) and (grid[nodeRow][nodeCol + 1] == "1") and (nodeRow,nodeCol + 1) not in seen:
                            queue.append((nodeRow,nodeCol + 1))
        return numIslands
                        


                        


        
        
        #
        #
        