class Solution:
    def solveSudoku(self, board):
        def isValid(r, c, val):
            # Check row & column
            for i in range(9):
                if board[r][i] == val: return False
                if board[i][c] == val: return False

            # Check 3x3 sub-box
            startRow, startCol = (r // 3) * 3, (c // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[startRow + i][startCol + j] == val:
                        return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in map(str, range(1, 10)):
                            if isValid(r, c, num):
                                board[r][c] = num
                                if backtrack():
                                    return True
                                board[r][c] = "."  # undo choice
                        return False
            return True  # solved

        backtrack()
