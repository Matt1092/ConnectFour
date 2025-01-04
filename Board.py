"""
Module name: Board.py
Author: Matthew Moga
Date: January 5, 2024
Description: This class models the Connect-four board for our game. All methods required to manipulate the board are found here.
"""

class Board:
    """
    A class representing a Connect Four board.

    Attributes:
        rows (int): The rows of the board.
        cols (int): The columns of the board.
        emptyCells (int): The empty cells of the board.
        board (char array): 2D character array of the board.
    """
    ROWS = 6
    COLS = 7

    def __init__(self):
        """
        This function initializes all the instance variables.
        """
        self.rows = Board.ROWS
        self.cols = Board.COLS
        self.emptyCells = self.rows * self.cols
        self.board = [[' ' for x in range(self.cols)] for x in range(self.rows)]

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def getEmptyCells(self):
        return self.emptyCells

    def clearBoard(self):
        self.emptyCells = self.rows * self.cols
        self.board = [[' ' for x in range(self.cols)] for x in range(self.rows)]

    def printBoard(self):
        print("  0   1   2   3   4   5   6")
        print("-----------------------------")
        for i in range(self.rows):
            print("|", end="")
            for j in range(self.cols):
                print(f" {self.board[i][j]} |", end="")
            print("\n-----------------------------")

    def placeToken(self, col, token):
        if not isinstance(col, int) or col < 0 or col >= self.getCols():
            return False

        for row in range(self.getRows() - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = token
                self.emptyCells -= 1
                return True
        return False

    def check_line(self, start_row, start_col, delta_row, delta_col, playerSymbol):
        for i in range(4):
            if not (0 <= start_row < self.rows and 0 <= start_col < self.cols):
                return False
            if self.board[start_row][start_col] != playerSymbol:
                return False
            start_row += delta_row
            start_col += delta_col
        return True

    def checkWinner(self, playerSymbol):
        for row in range(self.getRows()):
            for col in range(self.getCols()):
                if (self.check_line(row, col, 0, 1, playerSymbol) or  # Horizontal
                    self.check_line(row, col, 1, 0, playerSymbol) or  # Vertical
                    self.check_line(row, col, 1, 1, playerSymbol) or  # Diagonal /
                    self.check_line(row, col, 1, -1, playerSymbol)):  # Diagonal \
                    return True
        return False

    def checkAcross(self, row):
        for col in range(self.getCols() - 2):
            if self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col + 2] == 'X' or self.board[row + 1][col + 2] == 'O')):
                return col + 2
            elif self.board[row][col] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col] == 'X' or self.board[row + 1][col] == 'O')) and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X':
                return col
            elif self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == ' ':
                return col + 2
            elif self.board[row][col] == ' ' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X':
                return col
        return -1

    def checkVertical(self, col):
        for row in range(self.getRows() - 2):
            if self.board[row + 2][col] == 'X' and self.board[row + 1][col] == 'X' and self.board[row][col] == ' ':
                return True
        return False

    def blockVertical(self, col):
        for row in range(self.getRows() - 3):
            if self.board[row + 3][col] == 'X' and self.board[row + 2][col] == 'X' and self.board[row + 1][col] == 'X' and self.board[row][col] == ' ':
                return True
        return False

    def blockAcross(self, row):
        for col in range(self.getCols() - 3):
            if self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col + 3] == 'X' or self.board[row + 1][col + 3] == 'O')):
                return col + 3
            elif self.board[row][col] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col] == 'X' or self.board[row + 1][col] == 'O')) and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == 'X':
                return col
            elif self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == ' ':
                return col
            elif self.board[row][col] == ' ' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == 'X':
                return col
        return -1

    def checkWinAcross(self, row):
        for col in range(self.getCols() - 3):
            if self.board[row][col] == 'O' and self.board[row][col + 1] == 'O' and self.board[row][col + 2] == 'O' and self.board[row][col + 3] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col + 3] == 'X' or self.board[row + 1][col + 3] == 'O')):
                return col + 3
            elif self.board[row][col] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col] == 'X' or self.board[row + 1][col] == 'O')) and self.board[row][col + 1] == 'O' and self.board[row][col + 2] == 'O' and self.board[row][col + 3] == 'O':
                return col
            elif self.board[row][col] == 'O' and self.board[row][col + 1] == 'O' and self.board[row][col + 2] == 'O' and self.board[row][col + 3] == ' ':
                return col
            elif self.board[row][col] == ' ' and self.board[row][col + 1] == 'O' and self.board[row][col + 2] == 'O' and self.board[row][col + 3] == 'O':
                return col
        return -1

    def checkWinVertical(self, col):
        for row in range(self.getRows() - 3):
            if self.board[row + 3][col] == 'O' and self.board[row + 2][col] == 'O' and self.board[row + 1][col] == 'O' and self.board[row][col] == ' ':
                return True
        return False

    def computerAttack(self):
        """
        This function implements the above helper functions to determine the best possible computer move.

        Returns:
            int: Specified column to place the 'O'.
        """
        # Check for potential horizontal winning move
        for row in range(self.getRows()):
            if self.checkWinAcross(row) != -1:
                return self.checkWinAcross(row)
        
        # Check for potential vertical winning move
        for col in range(self.getCols()):
            if self.checkWinVertical(col):
                return col
        
        # Check for win stopping blocks (horizontal and vertical)
        for row in range(self.getRows()):
            if self.blockAcross(row) != -1:
                return self.blockAcross(row)
        for col in range(self.getCols()):
            if self.blockVertical(col):
                return col

        # Check for strategic horizontal blocks
        for row in range(self.getRows()):
            if self.checkAcross(row) != -1:
                return self.checkAcross(row)
        
        # Check for strategic vertical blocks
        for col in range(self.getCols()):
            if self.checkVertical(col):
                return col

        # Make random move otherwise (ensuring cell is empty)
        for row in range(self.getRows() - 1, -1, -1):
            for col in range(self.getCols()):
                if self.board[row][col] == ' ':
                    return col

    def __str__(self):
        return f"Statistics: \nThere are: {self.getEmptyCells()} empty cells."
