class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        ans = [0,0]
        values = {i:0 for i in range(1,(rows * cols)+1) }

        for row in range(rows):
            for col in range(cols):
                values[grid[row][col]] += 1
        for key ,value in values.items():
            if value > 1:
                ans[0] = key
            elif value == 0:
                ans[1] = key

        return ans
                

        print(values)