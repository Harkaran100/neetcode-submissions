class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        minRow = 0
        maxRow = len(matrix) -1

        # do code to find correct row
        while minRow <= maxRow:
            midRow = (maxRow + minRow) // 2
            if matrix[midRow][0] <= target <= matrix[midRow][-1]:
                # correct row located
                break
            elif target > matrix[midRow][-1]:
                minRow = midRow + 1
            elif target < matrix[midRow][0]:
                maxRow = midRow - 1

        # code to find correct col
        left = 0
        right = len(matrix[midRow]) -1
        while left <= right:
            midCol = (right + left) // 2
            midVal = matrix[midRow][midCol]
            if target == midVal:
                return True
            elif target > midVal:
                left = midCol + 1
            elif target < midVal:
                right = midCol - 1
        return False

        # instead of min and max for rows and cols
        # how about do binarySearch so identifyRow, the do again for col?
        # but how to do on row when its not a exact value?

