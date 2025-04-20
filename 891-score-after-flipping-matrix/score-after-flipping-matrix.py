class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        # flip rows
        for row in range(rows):
            if grid[row][0] == 0:
                for col in range(cols):
                    grid[row][col] = 0  if grid[row][col] else 1

        # flip cols

        for col in range(cols):
            one_count = 0
            for row in range(rows):
                one_count += grid[row][col]

            if one_count < rows - one_count:
                for row in range(rows):
                    grid[row][col] = 0 if grid[row][col] else 1
        for row in grid:
            num = "".join(str(x) for x in row)
            res += int(num,2)

        return res