class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        rows = len(mat)
        cols = len(mat[0])
        row = 0
        col = 0
        def is_valid(row, col, rows, cols):
            return 0 <= row < rows and 0 <= col < cols  
        while len(ans) < rows * cols:
            while True:
                temp_row = row
                temp_col = col
                if is_valid(row,col,rows,cols):
                    ans.append(mat[row][col])
                row -= 1
                col += 1
                if not is_valid(row,col,rows,cols):
                    row = temp_row
                    col = temp_col + 1
                    break

            while True:
                temp_row = row
                temp_col = col
                if is_valid(row,col,rows,cols):
                    ans.append(mat[row][col])
                row += 1
                col -= 1
                if not is_valid(row,col,rows,cols):
                    row = temp_row +1
                    col = temp_col 
                    break
        return ans
