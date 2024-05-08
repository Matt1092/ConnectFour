#This class models the Connect-four board for our game.
#All methods required to manipulate the board are found here.
#author Matthew Moga
#version December 14, 2022

import random

class Board:
    def __init__(self):
        # Properly encapsulated (private) instance variables
        self.rows = 6
        self.cols = 7
        self.emptyCells = self.rows * self.cols

        #Design Decision: I will represent the Board using an array of char(acters) rather than Strings.
        #Since char is a primitive data type it uses less memory and we can use == for comparisons.
        self.board = [[' ' for x in range(self.cols)] for x in range(self.rows)]

    #This accessor returns the number of rows on the board.
    def getRows(self):
        return self.rows
    
    
    #This accessor returns the number of columns on the board.
    def getCols(self):
        return self.cols


    #This accessor returns the number of free cells left on the board.
    def getEmptyCells(self):
        return self.emptyCells
    

    #This mutator initializes all board indices with empty characters.
    def clearBoard(self):
        #Fill the board with blank spaces
        self.emptyCells = self.rows * self.cols
        self.board = [[' ' for x in range(self.cols)] for x in range(self.rows)]

    
    #This method will print a Connect-Four board.
     #This method has no parameters and returns nothing.
    def printBoard(self):
        print("  0   1   2   3   4   5   6")
        print("-----------------------------")
        for i in range(self.rows):
            print("|", end = "")
            for j in range(self.cols):
                print(f" {self.board[i][j]} |", end = "")
            print("\n-----------------------------")
    

    #This method attempts to place a given player token on the board.  
    #It checks that the given row and col are valid indices and also that the chosen cell is ' ' empty.
    #If so, it places the given token in that cell, and returns true.
    #Otherwise, it does not change the board and returns false.
    def placeToken(self, col, token):

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
    
    
    #This method checks if there are 4 'X' or 4 'O' characters in a row (vertically, horizontally, or diagonally) on the board.
    def checkWinner(self, playerSymbol):
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
    

    #This method checks if there are 2 'X' characters in a row, horizontally on the board.
    def checkAcross(self, row):
        for col in range(self.getCols() - 2):
            #Remember to check if the row beneath the empty cell is either an X or an O (otherwise, this blocking strategy would be pointless)
            if self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col + 2] == 'X' or self.board[row + 1][col + 2] == 'O')):
                return col + 2
            #Same checking as above
            elif self.board[row][col] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col] == 'X' or self.board[row + 1][col] == 'O')) and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X':
                return col
        return -1

    
    #This method checks if there are 2 'X' characters in a row or 3, vertically on the board.
    def checkVertical(self, col):
        for row in range(self.getRows() - 3):
            if (((self.board[row + 3][col] == 'X') and (self.board[row + 2][col] == 'X') and (self.board[row + 1][col] == 'X') and (self.board[row][col] == ' '))):
                return True
        for row in range(self.getRows() - 2):
            if (((self.board[row + 2][col] == 'X') and (self.board[row + 1][col] == 'X') and (self.board[row][col] == ' '))):
                return True
        return False
    

    #This method checks if there is a singular 'O' character, horizontally on the board.
    def computerAttack(self):
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



    #Standard toString method.
    def __str__(self):
        return f"Statistics: \n" + "There are: " + str(self.getEmptyCells()) + " empty cells."
