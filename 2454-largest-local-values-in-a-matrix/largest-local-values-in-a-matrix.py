class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        ans = [[0 for col in range(cols-2)] for row in range(rows-2)]
        print(ans)
        for row in range(rows-2):
            for col in range(cols-2):
                max_val = 0
                for r in range(row, row+3):
                    for c in range(col, col+3):
                        max_val = max(max_val, grid[r][c])
                ans[row][col] = max_val
                
        return ans

      

