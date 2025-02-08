class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        for row in range(rows):
            for col in range(row + 1,rows): 
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        for row in matrix:
            row.reverse()

        