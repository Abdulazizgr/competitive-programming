class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_valid(r,c):
            return 0 <= r < rows and 0 <= c < cols
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    ans += 4
                    for r ,c in directions:
                        nr = r + row
                        nc = c + col
                        if is_valid(nr,nc):
                            if grid[nr][nc] == 1:
                                ans -= 1
        return ans 