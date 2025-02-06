class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row < len(matrix)-1 and col < len(matrix[0]) -1:
                    if matrix[row][col] != matrix[row+1][col+1]:
                        return False
        return True
          