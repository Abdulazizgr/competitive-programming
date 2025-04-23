class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            row.sort()

        for col in range(len(grid[0])):
            max_num = 0
            for row in range(len(grid)):
                max_num = max(max_num,grid[row][col])
            ans += max_num
        

        return ans