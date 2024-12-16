class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        cols = len(mat[0])

        diag = defaultdict(list)

        for i in range(row):
            for j in range(cols):
                diag[j-i].append(mat[i][j])
        for key in diag:
            diag[key].sort()
        for i in range(row):
            for j in range(cols):
                mat[i][j] = diag[j-i].pop(0) 
        return mat
















        # rows, cols = len(mat), len(mat[0])
        # diagonals = defaultdict(list)  

        # for i in range(rows):
        #     for j in range(cols):
        #         diagonals[j - i].append(mat[i][j])
        #         # print(mat[i][j])
        #     # print()

        # # Step 2: Sort each diagonal
        # for key in diagonals:
        #     diagonals[key].sort()
        # print(diagonals)

        # # Step 3: Write back the sorted diagonals to the matrix
        # for i in range(rows):
        #     for j in range(cols):
        #         mat[i][j] = diagonals[j - i].pop(0)

        # return mat