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

    def __str__(self):
        return f"Statistics: \n" + "There are: " + str(self.getEmptyCells()) + " empty cells."
