class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row_low, row_high = 0, rows - 1
        
        while row_low <= row_high:
            row_mid = (row_low + row_high) // 2
            if matrix[row_mid][0] <= target <= matrix[row_mid][cols - 1]:
                break
            elif target < matrix[row_mid][0]:
                row_high = row_mid - 1
            else:
                row_low = row_mid + 1
        
        if row_low > row_high:
            return False
        

        col_low, col_high = 0, cols - 1
        while col_low <= col_high:
            col_mid = (col_low + col_high) // 2
            if matrix[row_mid][col_mid] == target:
                return True
            elif target < matrix[row_mid][col_mid]:
                col_high = col_mid - 1
            else:
                col_low = col_mid + 1
        
        return False