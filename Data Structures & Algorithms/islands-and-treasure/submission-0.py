class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # get len
        rows = len(grid)
        cols = len(grid[0])

        # set
        visited = set()

        # queue
        q = deque()

        # first loop to populate queue with all chests
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))

        distance = 0

        def addcell(r,c):
            # out of bounds
            if (r < 0) or (r >= rows) or (c < 0) or (c >= cols):
                return 0
            # can't traverse
            elif grid[r][c] == -1:
                return
            # in visited
            elif (r,c) in visited:
                return
            else:
                visited.add((r,c))
                q.append((r,c))

            

        while q: # until queue is empty
            # 1 level at a time
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance

                # bfs
                addcell(r - 1,c) # up
                addcell(r + 1,c) # down
                addcell(r,c - 1) # left
                addcell(r,c + 1) # right

            distance += 1



        
        
        
        # iterate through
        # if come across -1 keep iterating
        # if come across -inf do nothing keep iterating
        # if come across 0
        # mark it
        # do this through entire grid
        # then start bfs on all chests at the same time going to valid paths
        # do this one at a time and replace that value with how long it took to get there
        # do this until all possible visitibly 
        # indexes are visited
        