class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        row_counts = [0] * rows  
        col_counts = [0] * cols  
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    row_counts[row] += 1
                    col_counts[col] += 1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]== 1 and(row_counts[row] > 1 or col_counts[col] > 1):
                    ans += 1
        
        return ans
    
        