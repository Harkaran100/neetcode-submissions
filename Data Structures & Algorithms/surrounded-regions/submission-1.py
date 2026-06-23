class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(row,col):
           # out of bounds
            if (row < 0) or (row >= rows) or (col < 0) or (col >= cols):
                return
            # visited
            if (row,col) in visited:
                return
            # values other then O
            if board[row][col] != "O":
                return
            board[row][col] = "T"
            visited.add((row,col))

            dfs(row - 1,col)
            dfs(row + 1,col)
            dfs(row,col -1 )
            dfs(row,col + 1)


        # top and bottom loop
        for c in range(cols):
            if board[0][c] =="O":
                dfs(0,c)
            if board[rows - 1][c] =="O":
                dfs(rows - 1,c)
        for r in range(rows):
            if board[r][0] =="O":
                dfs(r,0)
            if board[r][cols -1] =="O":
                dfs(r,cols - 1)
        

        # make all non border connecting os into x
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # make all T's back to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"


        #do a for loop on all corners,
        # if o do a dfs and find all os
        # mean while doing this turn all o to t
        # once done do forloop to turn all remaining os to x
        # do forlooop to turn all ts into o