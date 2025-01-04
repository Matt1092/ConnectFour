import random

class Board:
    ROWS = 6
    COLS = 7
    WIN_CONDITION = 4

    def __init__(self):
        self.rows = Board.ROWS
        self.cols = Board.COLS
        self.emptyCells = self.rows * self.cols
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def getEmptyCells(self):
        return self.emptyCells

    def clearBoard(self):
        self.emptyCells = self.rows * self.cols
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]

    def printBoard(self):
        print("  0   1   2   3   4   5   6")
        print("-----------------------------")
        for i in range(self.rows):
            print("|", end="")
            for j in range(self.cols):
                print(f" {self.board[i][j]} |", end="")
            print("\n-----------------------------")

    def placeToken(self, col, token):
        if col < 0 or col >= self.getCols():
            return False

        for row in range(self.getRows() - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = token
                self.emptyCells -= 1
                return True
        return False

    def checkWinner(self, playerSymbol):
        for row in range(self.getRows()):
            for col in range(self.getCols() - Board.WIN_CONDITION + 1):
                if all(self.board[row][col + i] == playerSymbol for i in range(Board.WIN_CONDITION)):
                    return True

        for row in range(self.getRows() - Board.WIN_CONDITION + 1):
            for col in range(self.getCols()):
                if all(self.board[row + i][col] == playerSymbol for i in range(Board.WIN_CONDITION)):
                    return True

        for row in range(self.getRows() - Board.WIN_CONDITION + 1):
            for col in range(self.getCols() - Board.WIN_CONDITION + 1):
                if all(self.board[row + i][col + i] == playerSymbol for i in range(Board.WIN_CONDITION)):
                    return True

        for row in range(Board.WIN_CONDITION - 1, self.getRows()):
            for col in range(self.getCols() - Board.WIN_CONDITION + 1):
                if all(self.board[row - i][col + i] == playerSymbol for i in range(Board.WIN_CONDITION)):
                    return True

        return False

    def checkAcross(self, row):
        for col in range(self.getCols() - 2):
            if self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col + 2] in ['X', 'O'])):
                return col + 2
            elif self.board[row][col] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col] in ['X', 'O'])) and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X':
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
            if self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col + 3] in ['X', 'O'])):
                return col + 3
            elif self.board[row][col] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col] in ['X', 'O'])) and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == 'X':
                return col
            elif self.board[row][col] == 'X' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == ' ':
                return col
            elif self.board[row][col] == ' ' and self.board[row][col + 1] == 'X' and self.board[row][col + 2] == 'X' and self.board[row][col + 3] == 'X':
                return col
        return -1

    def checkWinAcross(self, row):
        for col in range(self.getCols() - 3):
            if self.board[row][col] == 'O' and self.board[row][col + 1] == 'O' and self.board[row][col + 2] == 'O' and self.board[row][col + 3] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col + 3] in ['X', 'O'])):
                return col + 3
            elif self.board[row][col] == ' ' and ((row + 1 < self.getRows()) and (self.board[row + 1][col] in ['X', 'O'])) and self.board[row][col + 1] == 'O' and self.board[row][col + 2] == 'O' and self.board[row][col + 3] == 'O':
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
        for row in range(self.getRows()):
            result = self.checkWinAcross(row)
            if result != -1:
                return result

        for col in range(self.getCols()):
            if self.checkWinVertical(col):
                return col

        for row in range(self.getRows()):
            result = self.blockAcross(row)
            if result != -1:
                return result

        for col in range(self.getCols()):
            if self.blockVertical(col):
                return col

        for row in range(self.getRows()):
            result = self.checkAcross(row)
            if result != -1:
                return result

        for col in range(self.getCols()):
            if self.checkVertical(col):
                return col

        empty_cols = [col for col in range(self.getCols()) if self.board[0][col] == ' ']
        if empty_cols:
            return random.choice(empty_cols)
        else:
            raise Exception("No valid moves available")

    def __str__(self):
        return f"Statistics: \nThere are: {self.getEmptyCells()} empty cells."
