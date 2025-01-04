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
    def __init__(self):
        """
        This function initializes all the instance variables.
        """
        # Instance variables
        self.rows = 6
        self.cols = 7
        self.emptyCells = self.rows * self.cols

        #Design Decision: I will represent the Board using an array of char(acters) rather than Strings.
        #Since char is a primitive data type it uses less memory and we can use == for comparisons.
        self.board = [[' ' for x in range(self.cols)] for x in range(self.rows)]




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
        #Fill the board with blank spaces
        self.emptyCells = self.rows * self.cols
        self.board = [[' ' for x in range(self.cols)] for x in range(self.rows)]

    


    def printBoard(self):
        """
        This function will print a Connect-Four board.
        """
        print("  0   1   2   3   4   5   6")
        print("-----------------------------")
        for i in range(self.rows):
            print("|", end = "")
            for j in range(self.cols):
                print(f" {self.board[i][j]} |", end = "")
            print("\n-----------------------------")
    



    def placeToken(self, col, token):
        """
        This function attempts to place a given player token on the board.
        It checks that the given row and col are valid indices and also that the chosen cell is ' ' empty.
        If so, it places the given token in that cell, and returns true.
        Otherwise, it does not change the board and returns false.

        Args:
            col (int): Specified column to place token.
            token (char): 'X' or 'O' depending on user or computer move.
    
        Returns:
            bool: Returns True if location was valid and empty, returns False if location was invalid and filled.
        """

        #Invalid move, row is out of range (0..6) or the cell was not empty
        if col < 0 or col >= self.getCols():
            return False
        
        #Find the closest empty cell to the bottom in the specified column
        for row in range(self.getRows() - 1, -1, -1):
                if self.board[row][col] == ' ':
                    self.board[row][col] = token
                    self.emptyCells -= 1
                    return True
                
        #Return false if empty cell not found in column
        return False
    
    


    def checkWinner(self, playerSymbol):
        """
        This function checks if there are 4 'X' or 4 'O' characters in a row (vertically, horizontally, or diagonally) on the board.

        Args:
            playerSymbol (char): 'X' or 'O'.
    
        Returns:
            bool: Returns True if there are 4 'X''s ir 4 'O''s in a row, returns False if there is a tie between the player and the computer.
        """
        #check for 4 across
        for row in range(self.getRows()):
            for col in range(len(self.board[0]) - 3):
                if ((self.board[row][col] == playerSymbol) and
                    (self.board[row][col+1] == playerSymbol) and
                    (self.board[row][col+2] == playerSymbol) and
                    (self.board[row][col+3] == playerSymbol)):
                    return True

        #check for 4 up and down
        for row in range(self.getRows() - 3):
            for col in range(len(self.board[0])):
                if ((self.board[row][col] == playerSymbol) and
                    (self.board[row+1][col] == playerSymbol) and
                    (self.board[row+2][col] == playerSymbol) and
                    (self.board[row+3][col] == playerSymbol)):
                    return True

        #check upward diagonal
        for row in range(3, self.getRows()):
            for col in range(0, len(self.board[0]) - 3):
                if ((self.board[row][col] == playerSymbol) and
                    (self.board[row-1][col+1] == playerSymbol) and
                    (self.board[row-2][col+2] == playerSymbol) and
                    (self.board[row-3][col+3] == playerSymbol)):
                    return True

        #check downward diagonal
        for row in range(self.getRows() - 3):
            for col in range(0, len(self.board[0]) - 3):
                if ((self.board[row][col] == playerSymbol) and
                    (self.board[row+1][col+1] == playerSymbol) and
                    (self.board[row+2][col+2] == playerSymbol) and
                    (self.board[row+3][col+3] == playerSymbol)):
                    return True
        return False
    



    def checkAcross(self, row):
        """
        This function checks if there are 2 'X' characters in a row, horizontally on the board.

        Args:
            row (int): Specified row to check for 2 consecutive 'X''s.
    
        Returns:
            int: Returns col + 2 if there are 2 X's in a row horizontally and an empty character (' ').
                 Returns col if there is an empty character (' '), proceeding with two X's horizontally.
                 Returns -1 if conditions are not met.
        """
        for col in range(self.getCols() - 2):
            #Check if the row beneath the empty cell is either an X or an O so computer doesn't make silly move
            if self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col + 2] == 'X' or self.board[row + 1][col + 2] == 'O')):
                return col + 2

            elif self.board[row][col] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col] == 'X' or self.board[row + 1][col] == 'O')) and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X':
                return col
            
            #Check for an empty cell on the righthand side at the bottom of the board
            elif self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == ' ':
                return col + 2
            
            #Check for an empty cell on the lefthand side of the 2 horizontal X's
            elif self.board[row][col] == ' ' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X':
                return col
        return -1




    def checkVertical(self, col):
        """
        This function checks if there are 2 'X' characters in a row, vertically on the board.

        Args:
            col (int): Specified column to check for 2 consecutive 'X''s.
    
        Returns:
            bool: Returns True if there are 2 'X''s in a row, returns False if otherwise. 
        """
        for row in range(self.getRows() - 2):
            if (((self.board[row + 2][col] == 'X') and (self.board[row + 1][col] == 'X') and (self.board[row][col] == ' '))):
              return True
        return False

    


    def blockVertical(self, col):
        """
        This function checks if there are 3 'X' characters in a row, vertically on the board.

        Args:
            col (int): Specified column to check for 3 consecutive 'X''s.
    
        Returns:
            bool: Returns True if there are 3 'X''s in a row, returns False if otherwise.
        """
        for row in range(self.getRows() - 3):
            if (((self.board[row + 3][col] == 'X') and (self.board[row + 2][col] == 'X') and (self.board[row + 1][col] == 'X') and (self.board[row][col] == ' '))):
                return True
        return False
    



    def blockAcross(self, row):
        """
        This function checks if there are 3 'X' characters in a row, horizontally on the board.

        Args:
            row (int): Specified row to check for 3 consecutive 'X''s.
    
        Returns:
            int: Returns col + 3 if there are 3 X's in a row horizontally and an empty character (' ').
                 Returns col if there is an empty character (' '), proceeding with 3 X's horizontally.
                 Returns -1 if conditions are not met.
        """
        for col in range(self.getCols() - 3):
            #Check row beneath empty cell after 3 consecutive X's just to verify that a token can be placed for win block
            if self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col + 3] == 'X' or self.board[row + 1][col + 3] == 'O')):
                return col + 3
            
            elif self.board[row][col] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col] == 'X' or self.board[row + 1][col] == 'O')) and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == 'X':
                return col
            
            #Check for horizontal block on bottom row (disregarding anything beneath this row as it is the bottommost row)
            elif self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == ' ':
                return col
            
            #Check for horizontal block on bottom row if empty cell on the lefthand side proceeded by 3 consecutive X's
            elif self.board[row][col] == ' ' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == 'X':
                return col
        return -1



    
    def checkWinAcross(self, row):
        """
        This function checks if there are 3 'O' characters in a row, horizontally on the board.

        Args:
            row (int): Specified row to check for 3 consecutive 'O''s.
    
        Returns:
            int: Returns col + 3 if there are 3 O's in a row horizontally and an empty character (' ').
                 Returns col if there is an empty character (' '), proceeding with 3 O's horizontally.
                 Returns -1 if conditions are not met.
        """
        for col in range(self.getCols() - 3):
            #Check row beneath empty cell after 3 consecutive O's just to verify that a token can be placed for computer win
            if self.board[row][col] == 'O' and self.board[row][col + 1] == 'O' and self.board[row][col + 2] == 'O' and self.board[row][col + 3] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col + 3] == 'X' or self.board[row + 1][col + 3] == 'O')):
                return col + 3
            elif self.board[row][col] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col] == 'X' or self.board[row + 1][col] == 'O')) and self.board[row][col + 1] == 'O' and self.board[row][col + 2] == 'O' and self.board[row][col + 3] == 'O':
                return col
            #Check for horizontal win on bottom row (disregarding anything beneath this row as it is the bottommost row)
            elif self.board[row][col] == 'O' and self.board[row][col + 1] == 'O' and self.board[row][col + 2] == 'O' and self.board[row][col + 3] == ' ':
                return col
            elif self.board[row][col] == ' ' and self.board[row][col + 1] == 'O' and self.board[row][col + 2] == 'O' and self.board[row][col + 3] == 'O':
                return col
        return -1
    
    


    def checkWinVertical(self, col):
        """
        This function checks if there are 3 'O' characters in a row, vertically on the board.

        Args:
            row (int): Specified row to check for 3 consecutive 'O''s.
    
        Returns:
            bool: Returns True if there are 3 consecutive 'O''s, returns False otherwise.
        """
        for row in range(self.getRows() - 3):
            if (((self.board[row + 3][col] == 'O') and (self.board[row + 2][col] == 'O') and (self.board[row + 1][col] == 'O') and (self.board[row][col] == ' '))):
                return True
        return False

    


    def computerAttack(self):
        """
        This function implements the above helper functions to determine the best possible computer move.

        Returns:
            col (int): Specified column to place the 'O'.
        """

        #Check for potential horizontal winning move
        for row in range(self.getRows()):
            if self.checkWinAcross(row) != -1:
                return self.checkWinAcross(row)
        
        #Check for potential vertical winning move
        for col in range(self.getCols()):
            if self.checkWinVertical(col):
                return col
        
        #Check for win stopping blocks (horizontal and vertical)
        for row in range(self.getRows()):
            if self.blockAcross(row) != -1:
                return self.blockAcross(row)
        for col in range(self.getCols()):
            if self.blockVertical(col):
                return col

        #Check for strategic horizontal blocks
        for row in range(self.getRows()):
            if self.checkAcross(row) != -1:
                return self.checkAcross(row)
        
        #Check for strategic vertical blocks
        for col in range(self.getCols()):
            if self.checkVertical(col):
                return col

        #Make random move otherwise (ensuring cell is empty)
        for row in range(self.getRows() - 1, -1, -1):
            for col in range(self.getCols()):
                if self.board[row][col] == ' ':
                    return col




    def __str__(self):
        """
        Python implementation of the toString() method.

        Returns:
            str: Statistics of the match (empty cells remaining).
        """
        return f"Statistics: \n" + "There are: " + str(self.getEmptyCells()) + " empty cells."
