class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed_mat = [[0]*len(matrix) for col in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                transposed_mat[col][row] = matrix[row][col]
        return transposed_mat