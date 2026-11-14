class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search of first col of each row
        rowLen = len(matrix)

        left = 0
        right = rowLen - 1

        firstVal = 0
        lastVal = len(matrix[0]) - 1

        correctRow = -1

        # get row
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][firstVal] <= target <= matrix[mid][lastVal]: # check row
                correctRow = mid
                break
            elif matrix[mid][firstVal] > target:# check below
                right = mid - 1
            elif target > matrix[mid][lastVal]:
                left = mid + 1
        if correctRow == -1: # early stopage
            return False

        while firstVal <= lastVal:
            mid = (firstVal + lastVal) // 2

            if matrix[correctRow][mid]  == target:
                return True
            elif matrix[correctRow][mid] > target:
                lastVal = mid - 1
            else:
                firstVal = mid + 1
        return False
        

