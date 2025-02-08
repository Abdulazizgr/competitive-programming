class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_neighbors(row, col):
            return [
                (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
                (row - 1, col - 1), (row + 1, col + 1), (row - 1, col + 1), (row + 1, col -1)
            ]  
        for row in range(9):
            horizontal = set()
            vertical = set()
            for col in range(9):
                if board[row][col].isdigit():
                    if board[row][col] not in horizontal :
                        horizontal.add(board[row][col])
                    else:
                        return False
                if board[col][row].isdigit():
                    if board[col][row] not in vertical :
                        vertical.add(board[col][row])
                    else:
                        return False
        
        middle_points = [
        (1,1), (1,4), (1,7),
        (4,1), (4,4), (4,7),
        (7,1), (7,4), (7,7) ]

        for row,col in middle_points:
            sub_box = set()
            if board[row][col].isdigit():
                sub_box.add(board[row][col])
            neighbors = get_neighbors(row, col)
            for r, c in neighbors:
                if board[r][c].isdigit():
                    if board[r][c] not in sub_box :
                        sub_box.add(board[r][c])
                    else:
                        return False

        
        return True
        


        