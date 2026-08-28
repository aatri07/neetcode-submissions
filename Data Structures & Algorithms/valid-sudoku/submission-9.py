class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dupes = set()
        col_dupes = set()
        square_dupes = set()

        for i in range(len(board)):
            row_dupes = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_dupes:
                    return False
                row_dupes.add(board[i][j])
            
        
        for i in range(len(board[0])):
            col_dupes = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] in col_dupes:
                    return False
                col_dupes.add(board[j][i])
            
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                square_dupes = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        val = board[i][j]
                        if val == '.':
                            continue
                        if val in square_dupes:
                            return False
                        square_dupes.add(val)


        return True

        
        