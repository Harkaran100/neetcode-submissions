class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # make sure each row, col or box doesnt have repeated characterss
        # we can acccomplish this by hashset.
        # make a hashset per row, col and box, so 9 for each
        rowSets = [set() for _ in range(9)] # _ because that var is never used
        colSets = [set() for _ in range(9)]
        boxSets = [set() for _ in range(9)]

        #now iterate through each value and add to the set for row, col and box
        # if its '.' then skip, else check if value exists in any set, if does return false
        # if doesnt add to 3 sets
        # how to iterate

        for row in range(9):
            for col in range(9):
                box = (row // 3) * 3 + (col // 3)
                value = board[row][col]
                # skip
                if value == ".":
                    continue
                if value in rowSets[row] or value in colSets[col] or value in boxSets[box]:
                    return False
                rowSets[row].add(value)
                colSets[col].add(value)
                boxSets[box].add(value)
        return True
