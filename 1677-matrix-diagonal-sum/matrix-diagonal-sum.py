class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        _sum = 0
        for i in range(n):
            _sum += mat[i][i] + mat[i][n - i - 1]
        if n % 2 == 1:
            _sum -= mat[n // 2][n // 2]
        return _sum