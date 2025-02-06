class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                val = matrix[row][col]
                if val == 0:
                    ans.append([row,col])
        for i in range(len(ans)):
            for j in range(len(matrix)):
                matrix[j][ans[i][1]] = 0
            for k in range(len(matrix[0])):
                matrix[ans[i][0]][k] = 0

            
                   
        return matrix
