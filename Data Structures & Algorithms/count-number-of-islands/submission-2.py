class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(row,col):
            queue = deque()
            queue.append((row,col))
            while queue:
                row, col = queue.popleft()
                directions = [(row + 1, col),(row - 1, col),(row, col + 1),(row, col - 1)]
                for r,c in directions: # check in range, not in visited, land
                    if (0 <= r < lenRow and 0 <= c < lenCol) and (r,c) not in visited and grid[r][c] == "1":
                        queue.append((r,c))
                        visited.add((r,c))

        if not grid:
            return 0
        lenRow = len(grid)
        lenCol = len(grid[0])
        visited = set()
        numIslands = 0
        for row in range(lenRow):
            for col in range(lenCol):
                if grid[row][col] == "1" and (row,col) not in visited:
                    numIslands += 1
                    visited.add((row,col))
                    bfs(row,col)
        return numIslands

        
        
        