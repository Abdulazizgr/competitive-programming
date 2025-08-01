class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rule 1 and rule 2

        for row in range(9):
            horizontal = set()
            vertical = set()
            for col in range(9):
                if board[row][col].isdigit():
                    if board[row][col] not in horizontal:
                        horizontal.add(board[row][col])
                    else:
                        return False
                if board[col][row].isdigit():
                    if board[col][row] not in vertical:
                        vertical.add(board[col][row])
                    else:
                        return False

        # rule 3
        middle_points = [
            (1,1),(1,4),(1,7),
            (4,1),(4,4),(4,7),
            (7,1),(7,4),(7,7)
        ]

        def get_neighbors(row,col):
            return [
                (row-1,col-1),(row-1,col),(row-1,col+1),
                (row,col+1),(row+1,col+1),(row+1,col),
                (row+1,col-1),(row,col-1)
            ]
        for row,col in middle_points:
            sub_box = set()
            if board[row][col].isdigit():
                sub_box.add(board[row][col])
            negihborbs = get_neighbors(row,col)
            for ro ,co in negihborbs:
                if board[ro][co].isdigit():
                    if board[ro][co] not in sub_box:
                        sub_box.add( board[ro][co])
                    else:
                        return False
        return True 
                    