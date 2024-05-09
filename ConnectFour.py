"""
Module name: ConnectFour.py
Author: Matthew Moga
Date: January 5, 2024
Description: This class models the Connect Four main loop for our game. All in game moves are found here.
"""




#Import statement to get Board from Board.py
from Board import Board




class ConnectFour:
    """
    A class representing the mainline logic of our Connect-Four game.

    Attributes:
        connectFourBoard (char array): The board that will be used for the in game moves.
        playGame (bool): Boolean variable used to determine status of game.
        gameLoop (bool): Boolean variable used to determine whether program keeps running or not.
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
        #Instantiate board
        connectFourBoard = Board()
        print("\nWelcome to Connect-Four!\n")
        playGame = False
        gameLoop = False
        #Prompt user for name
        name = input("What is your name? ")
        
        #Prompt user for yes or no response
        answer = input("\nYou ready for a challenge, " + name + "?\n(...YES or NO...) ")
        if answer.lower() == "yes" or "yes" in answer:
            #Start game
            print("\nPrepare yourself for the greatest match of Connect-Four...\n")
            playGame = True
            gameLoop = True
        
        #Exit game loop
        elif answer.lower() == ("no") or "no" in answer:
            print("\nUnfortunate. Practice more and then come back...\n")
        else:
            print("\nNot sure what you mean there, " + name + ". Get serious then come back!!!\n")
        
        #Mainline logic
        while (gameLoop):
            playGame = True
            while (playGame):
                usersTurn = True
                connectFourBoard.printBoard()
                print(str(connectFourBoard))
                if usersTurn:
                    ConnectFour.makeUserMove(connectFourBoard)
                    ConnectFour.makeComputerMove(connectFourBoard)
                        
                usersTurn = not usersTurn
                #Win scenario
                if connectFourBoard.checkWinner('X') == True:
                    print("YOU Won!  Congratulations.\n")
                    playGame = False

                #Lose scenario
                elif connectFourBoard.checkWinner('O') == True:
                    print("You LOSE!  Heehee!\n")
                    playGame = False

                #Draw scenario
                else:
                    if connectFourBoard.getEmptyCells() == 0:
                        print("Tie!  Try harder!\n")
                        playGame = False

            print("*** G A M E   O V E R ***")
            connectFourBoard.printBoard()
            connectFourBoard.clearBoard()
            #Ask user to play again
            gameLoop = ConnectFour.askPlayAgain()
                  



    @staticmethod
    def makeUserMove(connectFourBoard):
        """
        This function prompts the user for a move. When this function exits, an 'X' will be placed on the board in a valid (empty) cell.

        Args:
            connectFourBoard (char array): Board that is used to place 'X' token on.
        """
        validMove = False
            
        #Prompt for a row and column with input validation
        while not validMove:
            col = int(input("What column would you like to move to (0-6): "))
            #placeToken() will return false if the col is invalid or the cell is not empty
            validMove = connectFourBoard.placeToken(col, 'X')
            if not validMove:
                print("Sorry, that location is not available to place an 'X'.\n")
        



    @staticmethod
    def makeComputerMove(connectFourBoard):
        """
        This method generates a computer move with the use of CPU education and advanced machine learning. When this method exits, an 'O' will be placed on the board in a valid (empty) cell.

        Args:
            connectFourBoard (char array): Board that is used to place 'O' token on.
        """
        validMove = False
        col = -1                
            
        #Generate computer move, the column where we find an empty cell to place an 'O'
        while not validMove:
            col = connectFourBoard.computerAttack()
            validMove = connectFourBoard.placeToken(col, 'O')
        



    @staticmethod
    def askPlayAgain():
        """
        This function prompts the user if they would like to play again with some input validation.
        """
        playAgain = input("Play again? [y/n]: ")
        while (not playAgain == ("y") and not playAgain == ("yes") and not playAgain == ("n") and not playAgain == ("no")):
            playAgain = input("Play again? [y/n]: \n")

        if ((playAgain == ("y")) or (playAgain == ("yes"))):
            return True
        return False




#Call the main method
ConnectFour.main()
