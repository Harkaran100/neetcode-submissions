class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # split into 3 catgories
        # column, row and box
        # use hashset for this, find a way to ignore ., anything else in hashset
        # if in hashset already for this category then return not valid

        # create 27 hashsets
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

    
        # iterate through the sudoku board
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                # ignore .
                if value == ".":
                    continue
                # check all hashmaps
                box_calc = (r // 3) * 3 + (c // 3)
                if value in rows[r] or value in cols[c] or value in box[box_calc]:
                    return False
                else:
                    # add to hashmap
                    rows[r].add(value)
                    cols[c].add(value)
                    box[box_calc].add(value)
    
        return True
