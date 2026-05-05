class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            currRow = set()
            for j in range(9):
                if board[i][j] == '.': continue
                if board[i][j] in currRow: return False
                currRow.add(board[i][j])

        for j in range(9):
            currCol = set()
            for i in range(9):
                if board[i][j] == '.': continue
                if board[i][j] in currCol: return False
                currCol.add(board[i][j])

        for r in range(3):
            for c in range(3):
                currSq = set()
                for i in range(3):
                    for j in range(3):
                        x = r * 3 + i
                        y = c * 3 + j
                        if board[x][y] == '.': continue
                        if board[x][y] in currSq: return False
                        currSq.add(board[x][y])

        return True