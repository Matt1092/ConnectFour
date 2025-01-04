"""
Module name: Board.py
Author: Matthew Moga
Date: January 5, 2024
Description: This class models the Connect-four board for our game. All methods required to manipulate the board are found here.
"""

import random

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
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]

    def getRows(self):
        """
        This accessor returns the number of rows on the board.

        Returns:
            int: The number of rows.
        """
        return self.rows

    def getCols(self):
        """
        This accessor returns the number of columns on the board.

        Returns:
            int: The number of columns.
        """
        return self.cols

    def getEmptyCells(self):
        """
        This accessor returns the number of free cells left on the board.

        Returns:
            int: The number of empty cells.
        """
        return self.emptyCells

    def clearBoard(self):
        """
        This mutator initializes all board indices with empty characters.
        """
        self.emptyCells = self.rows * self.cols
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]

    def printBoard(self):
        """
        This function will print a Connect-Four board.
        """
        print("  0   1   2   3   4   5   6")
        print("-----------------------------")
        for i in range(self.rows):
            print("|", end="")
            for j in range(self.cols):
                print(f" {self.board[i][j]} |", end="")
            print("\n-----------------------------")

    def placeToken(self, col, token):
        """
        This function attempts to place a given player token on the board.
        It checks that the given column is valid and also that the chosen cell is empty.
        If so, it places the given token in that cell and returns true.
        Otherwise, it does not change the board and returns false.

        Args:
            col (int): Specified column to place token.
            token (char): 'X' or 'O' depending on user or computer move.

        Returns:
            bool: Returns True if the location was valid and empty, returns False otherwise.
        """
        if not isinstance(col, int) or col < 0 or col >= self.getCols():
            print(f"Invalid column: {col}")
            return False

        for row in range(self.getRows() - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = token
                self.emptyCells -= 1
                return True
        print(f"Column {col} is full")
        return False

    def check_line(self, start_row, start_col, delta_row, delta_col, playerSymbol):
        """
        This function checks if there are 4 'X' or 'O' characters in a row (vertically, horizontally, or diagonally) on the board.

        Args:
            start_row (int): Starting row index.
            start_col (int): Starting column index.
            delta_row (int): Row increment.
            delta_col (int): Column increment.
            playerSymbol (char): 'X' or 'O'.

        Returns:
            bool: Returns True if there are 4 'X's or 4 'O's in a row, False otherwise.
        """
        for _ in range(4):
            if not (0 <= start_row < self.rows and 0 <= start_col < self.cols):
                return False
            if self.board[start_row][start_col] != playerSymbol:
                return False
            start_row += delta_row
            start_col += delta_col
        return True

    def checkWinner(self, playerSymbol):
        """
        This function checks if there is a winner on the board.

        Args:
            playerSymbol (char): 'X' or 'O'.

        Returns:
            bool: Returns True if there is a winner, False otherwise.
        """
        for row in range(self.getRows()):
            for col in range(self.getCols()):
                if (self.check_line(row, col, 0, 1, playerSymbol) or  # Horizontal
                    self.check_line(row, col, 1, 0, playerSymbol) or  # Vertical
                    self.check_line(row, col, 1, 1, playerSymbol) or  # Diagonal /
                    self.check_line(row, col, 1, -1, playerSymbol)):  # Diagonal \
                    return True
        return False

    def checkAcross(self, row):
        """
        This function checks if there are 2 'X' characters in a row, horizontally on the board.

        Args:
            row (int): Specified row to check for 2 consecutive 'X's.

        Returns:
            int: Returns column index if a strategic move is found, -1 otherwise.
        """
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
        """
        This function checks if there are 2 'X' characters in a row, vertically on the board.

        Args:
            col (int): Specified column to check for 2 consecutive 'X's.

        Returns:
            bool: Returns True if there are 2 'X's in a row, False otherwise.
        """
        for row in range(self.getRows() - 2):
            if self.board[row + 2][col] == 'X' and self.board[row + 1][col] == 'X' and self.board[row][col] == ' ':
                return True
        return False

    def blockVertical(self, col):
        """
        This function checks if there are 3 'X' characters in a row, vertically on the board.

        Args:
            col (int): Specified column to check for 3 consecutive 'X's.

        Returns:
            bool: Returns True if there are 3 'X's in a row, False otherwise.
        """
        for row in range(self.getRows() - 3):
            if self.board[row + 3][col] == 'X' and self.board[row + 2][col] == 'X' and self.board[row + 1][col] == 'X' and self.board[row][col] == ' ':
                return True
        return False

    def blockAcross(self, row):
        """
        This function checks if there are 3 'X' characters in a row, horizontally on the board.

        Args:
            row (int): Specified row to check for 3 consecutive 'X's.

        Returns:
            int: Returns column index if a blocking move is found, -1 otherwise.
        """
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
        """
        This function checks if there are 3 'O' characters in a row, horizontally on the board.

        Args:
            row (int): Specified row to check for 3 consecutive 'O's.

        Returns:
            int: Returns column index if a winning move is found, -1 otherwise.
        """
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
        """
        This function checks if there are 3 'O' characters in a row, vertically on the board.

        Args:
            col (int): Specified column to check for 3 consecutive 'O's.

        Returns:
            bool: Returns True if there are 3 'O's in a row, False otherwise.
        """
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
        empty_cols = [col for col in range(self.getCols()) if self.board[0][col] == ' ']
        if empty_cols:
            return random.choice(empty_cols)
        else:
            raise Exception("No valid moves available")

    def __str__(self):
        """
        Python implementation of the toString() method.

        Returns:
            str: Statistics of the match (empty cells remaining).
        """
        return f"Statistics: \nThere are: {self.getEmptyCells()} empty cells."
