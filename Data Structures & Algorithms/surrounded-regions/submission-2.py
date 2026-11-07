class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #lengths
        rows = len(board)
        cols = len(board[0])
        
        # safe set
        safe = set()

        # directions
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        def dfs(row,col):
            # add to safe
            safe.add((row,col))
            for dir in directions:
                r,c = dir
                newRow, newCol =  row + r , col + c
                if ((0 <= newRow < rows) and (0 <= newCol < cols) 
                and (newRow,newCol) not in safe and (board[newRow][newCol] == "O")):
                    dfs(newRow,newCol)

        # check all edges
        # top
        for c in range(cols):
            if board[0][c] == "O" and (0,c) not in safe:
                dfs(0,c)
        # bottom
        for c in range(cols):
            if board[rows -1][c] == "O" and (rows-1,c) not in safe:
                dfs(rows-1,c)
        # left
        for r in range(rows):
            if board[r][0] == "O" and (r,0) not in safe:
                dfs(r,0)
        # right
        for r in range(rows):
            if board[r][cols -1] == "O" and (r,cols-1) not in safe:
                dfs(r,cols-1)

        # change all none safe Os to xs
        for row in range(rows):
            for col in range(cols):
                if (row,col) not in safe and board[row][col] == "O":
                    board[row][col] = "X"

        return None





        # first thing comes to mind is look for those that are safe,
        # look at all esges if any marked with 0, add to safe and do dfs/ bfs to all conencted 0s such that those are safe
        #once we have done bfs from all 0s from edges 
        # also ensure while doing this that the new cell isnt already in safe to prevent double checking
        # once all of this is done
        # do a for loop for entire array any cell that isnt in safe set and is 0 change to x

        # if using bfs, can be o of m x n time for stack, and o of m x n for second last for loop and o of m + o of m + o of n + o of n initally when checking the edges
        # also o of m x n space for set

        # simplfieis to o of m x n time and o of m xn space
        