from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkBoxes(board)
    
    def checkRows(self,board):
        for row in board:
            seen=set()
            for val in row:
                if val!=".":
                    if val in seen:
                        return False
                    seen.add(val)
        return True
    
    def checkCols(self,board):
        for col in range(9):
            seen=set()
            for row in range(9):
                val=board[row][col]
                if val!=".":
                    if val in seen:
                        return False
                    seen.add(val)
        return True
    
    def checkBoxes(self,board):
        for box_row in range(3):
            for box_col in range(3):
                seen=set()
                for row in range(box_row*3,box_row*3+3):
                    for col in range(box_col*3,box_col*3+3):
                        val=board[row][col]
                        if val!=".":
                            if val in seen:
                                return False
                            seen.add(val)
        return True
s=Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                       ["6",".",".","1","9","5",".",".","."],
                       [".","9","8",".",".",".",".","6","."],
                       ["8",".",".",".","6",".",".",".","3"],
                       ["4",".",".","8",".","3",".",".","1"],
                       ["7",".",".",".","2",".",".",".","6"],
                       [".","6",".",".",".",".","2","8","."],
                       [".",".",".","4","1","9",".",".","5"],
                       [".",".",".",".","8",".",".","7","9"]]))        
print(s.isValidSudoku([["5","3","3",".","7",".",".",".","."],
                       ["6",".",".","1","9","5",".",".","."],
                       [".","9","8",".",".",".",".","6","."],
                       ["8",".",".",".","6",".",".",".","3"],
                       ["4",".",".","8",".","3",".",".","1"],
                       ["7",".",".",".","2",".",".",".","6"],
                       [".","6",".",".",".",".","2","8","."],
                       [".",".",".","4","1","9",".",".","5"],
                       [".",".",".",".","8",".",".","7","9"]]))        