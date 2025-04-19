class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0,0]
        rows = len(mat)
        cols = len(mat[0])
        one = [0] * rows
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    one[row] += 1
            if ans[1] < one[row]:
                ans = [row,one[row]]

        return ans 