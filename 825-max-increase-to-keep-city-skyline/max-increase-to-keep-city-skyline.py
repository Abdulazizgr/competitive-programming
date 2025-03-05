class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_col = []
        max_row = []
        _sum = 0
        for row in range(len(grid)):
            max_c = 0
            max_r = 0
            for col in range(len(grid)):
                max_c = max(max_c,grid[col][row])
                max_r = max(max_r,grid[row][col])
            max_col.append(max_c)
            max_row.append(max_r)
        for row in range(len(grid)):

            for col in range(len(grid)):
                _sum += min(max_col[row],max_row[col]) - grid[row][col]
        return _sum
