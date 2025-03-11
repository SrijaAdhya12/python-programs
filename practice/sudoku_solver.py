from string import digits
from typing import List

numbers = [digit for digit in digits[1:]]

class Solution:
    @staticmethod
    def is_valid(grid, num, row, col):
        for i in range(9):
            if num == grid[row][i]:
                return False
            if num == grid[i][col]:
                return False
        
        box_x = row // 3 * 3
        box_y = col // 3 * 3
        for i in range(box_x, box_x + 3):
            for j in range(box_y, box_y + 3):
                if grid[i][j] == num:
                    return False
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(10):
            if i == 9:
                return True
            for j in range(9):
                if board[i][j] != '.':
                    continue
                for num in numbers:
                    if self.is_valid(board, num, i, j):
                        board[i][j] = num
                        result = self.solveSudoku(board)
                        if result:
                            return True
                        board[i][j] = '.'
                return None
