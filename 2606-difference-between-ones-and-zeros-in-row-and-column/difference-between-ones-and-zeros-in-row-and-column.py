class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        one_row = [0] * rows
        one_col = [0] * cols

        zero_row = [0] * rows
        zero_col = [0] * cols

        diff = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    one_row[row] += 1
                    one_col[col] += 1
                else:
                    zero_row[row] += 1
                    zero_col[col] += 1
        for row in range(rows):
            for col in range(cols):
                diff[row][col] = one_row[row]+one_col[col] -zero_row[row]-zero_col[col]
                
        return diff
                