class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        min_num = [float('inf')] * rows
        max_num = [0] * cols
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] < min_num[row]:
                    min_num[row] = matrix[row][col]
                if matrix[row][col] > max_num[col]:
                   max_num[col]  =  matrix[row][col]
       
        min_num = set(min_num)
        for num in max_num:
            if num in min_num:
                return [num]
        return []