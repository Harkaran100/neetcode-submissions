class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # lengths of row and col
        rows = len(grid)
        cols = len(grid[0])

        # queue
        q = deque()
        #count
        minutes = 0
        # fresh fruit count
        fresh = 0
        #hashset
        visited = set()

        def bfs(r,c):
            nonlocal fresh
            # out of bounds 
            if (r < 0) or (r >= rows) or (c < 0) or (c >= cols):
                return
            # empty or rotten
            elif (grid[r][c] == 0) or (grid[r][c] == 2):
                return
            elif (r,c) in visited:
                return
            #fruit
            else:
                fresh -= 1
                visited.add((r,c))
                q.append((r,c))


        # loop to get rotten fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        # bfs portion
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                bfs(r - 1,c)
                bfs(r + 1,c)
                bfs(r,c - 1)
                bfs(r,c + 1)
            minutes += 1
        if fresh == 0:
            return minutes
        return -1

        