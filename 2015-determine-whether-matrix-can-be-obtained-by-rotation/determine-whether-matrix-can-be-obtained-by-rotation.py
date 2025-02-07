class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            for row in range(n):
                for col in range(row, n):
                    mat[row][col], mat[col][row] = mat[col][row], mat[row][col]
            for row in mat:
                row.reverse()
            if mat == target:
                return True
        return False
        
        


        print(mat)
       