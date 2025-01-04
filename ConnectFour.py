"""
Module name: ConnectFour.py
Author: Matthew Moga
Date: January 5, 2024
Description: This class models the Connect Four main loop for our game. All in game moves are found here.
"""

# Import statement to get Board from Board.py
from Board import Board

class ConnectFour:
    """
    A class representing the mainline logic of our Connect-Four game.

    Attributes:
        connectFourBoard (char array): The board that will be used for the in-game moves.
        playGame (bool): Boolean variable used to determine status of the game.
        gameLoop (bool): Boolean variable used to determine whether the program keeps running or not.
    """
    def __init__(self):
        """
        This function initializes all the instance variables (no instance variables).
        """
        pass

    @staticmethod
    def main():
        """
        This function defines the mainline logic for our game loop. It uses various helper methods to run the game.
        """
        connectFourBoard = Board()
        print("\nWelcome to Connect-Four!\n")
        playGame = False
        gameLoop = False

        # Prompt user for name
        name = input("What is your name? ")
        
        # Prompt user for yes or no response
        answer = input("\nYou ready for a challenge, " + name + "?\n(...YES or NO...) ")
        if answer.lower() == "yes" or "yes" in answer.lower():
            print("\nPrepare yourself for the greatest match of Connect-Four...\n")
            playGame = True
            gameLoop = True
        elif answer.lower() == "no" or "no" in answer.lower():
            print("\nUnfortunate. Practice more and then come back...\n")
        else:
            print("\nNot sure what you mean there, " + name + ". Get serious then come back!!!\n")
        
        while gameLoop:
            playGame = True
            while playGame:
                usersTurn = True
                connectFourBoard.printBoard()
                print(str(connectFourBoard))
                if usersTurn:
                    ConnectFour.makeUserMove(connectFourBoard)
                    ConnectFour.makeComputerMove(connectFourBoard)
                        
                usersTurn = not usersTurn

                # Check for win or draw scenarios
                if ConnectFour.check_winner(connectFourBoard, 'X'):
                    playGame = False
                elif ConnectFour.check_winner(connectFourBoard, 'O'):
                    playGame = False
                elif connectFourBoard.getEmptyCells() == 0:
                    print("Tie! Try harder!\n")
                    playGame = False

            print("*** G A M E   O V E R ***")
            connectFourBoard.printBoard()
            connectFourBoard.clearBoard()
            gameLoop = ConnectFour.askPlayAgain()

    @staticmethod
    def makeUserMove(connectFourBoard):
        """
        This function prompts the user for a move. When this function exits, an 'X' will be placed on the board in a valid (empty) cell.

        Args:
            connectFourBoard (char array): Board that is used to place 'X' token on.
        """
        validMove = False
        while not validMove:
            try:
                col = int(input("What column would you like to move to (0-6): "))
                validMove = connectFourBoard.placeToken(col, 'X')
                if not validMove:
                    print("Sorry, that location is not available to place an 'X'.\n")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 6.")

    @staticmethod
    def makeComputerMove(connectFourBoard):
        """
        This method generates a computer move with the use of CPU education and advanced machine learning. When this method exits, an 'O' will be placed on the board in a valid (empty) cell.

        Args:
            connectFourBoard (char array): Board that is used to place 'O' token on.
        """
        validMove = False
        while not validMove:
            col = connectFourBoard.computerAttack()
            validMove = connectFourBoard.placeToken(col, 'O')

    @staticmethod
    def askPlayAgain():
        """
        This function prompts the user if they would like to play again with some input validation.

        Returns:
            bool: True if the user wants to play again, False otherwise.
        """
        playAgain = input("Play again? [y/n]: ")
        while playAgain not in ("y", "yes", "n", "no"):
            playAgain = input("Play again? [y/n]: \n")
        return playAgain in ("y", "yes")

    @staticmethod
    def check_winner(connectFourBoard, symbol):
        """
        This function checks if the specified player has won.

        Args:
            connectFourBoard (Board): The game board.
            symbol (char): The player's symbol ('X' or 'O').

        Returns:
            bool: True if the player has won, False otherwise.
        """
        if connectFourBoard.checkWinner(symbol):
            if symbol == 'X':
                print("YOU Won! Congratulations.\n")
            else:
                print("You LOSE! Heehee!\n")
            return True
        return False

# Call the main method
ConnectFour.main()
