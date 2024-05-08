#This class models the Connect-four main loop for our game.
#All in game moves are found here.


import random
from Board import Board


class ConnectFour:
    def __init__(self):
        pass
    
    #This method defines the mainline logic for our game loop. 
    #It uses a Connect-Four Board object and various helper methods to run the game.
    @staticmethod
    def main():
        connectFourBoard = Board()
        print("\nWelcome to Connect-Four!\n")
        playGame = False
        gameLoop = False
        name = input("What is your name? ")
            
        answer = input("\nYou ready for a challenge, " + name + "?\n(...YES or NO...) ")
        if answer.lower() == "yes" or "yes" in answer:
            print("\nPrepare yourself for the greatest match of Connect-Four...\n")
            playGame = True
            gameLoop = True
        elif answer.lower() == ("no") or "no" in answer:
            print("\nUnfortunate. Practice more and then come back...\n")
        else:
            print("\nNot sure what you mean there, " + name + ". Get serious then come back!!!\n")
            
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
                if connectFourBoard.checkWinner('X') == True:
                    print("YOU Won!  Congratulations.\n")
                    playGame = False

                elif connectFourBoard.checkWinner('O') == True:
                    print("You LOSE!  Heehee!\n")
                    playGame = False

                else:
                    if connectFourBoard.getEmptyCells() == 0:
                        print("Tie!  Try harder!\n")
                        playGame = False

            print("*** G A M E   O V E R ***")
            connectFourBoard.printBoard()
            connectFourBoard.clearBoard()
            gameLoop = ConnectFour.askPlayAgain()
        
                
    #This method prompts the user for a move.
    #When this method exits, an 'X' will be placed on the board in a valid (empty) cell.
    @staticmethod
    def makeUserMove(connectFourBoard):
        validMove = False
            
        #Prompt for a row and column with input validation
        while not validMove:
            col = int(input("What column would you like to move to (0-6): "))
            #placeToken() will return false if the col is invalid or the cell is not empty
            validMove = connectFourBoard.placeToken(col, 'X')
            if not validMove:
                print("Sorry, that location is not available to place an 'X'.\n")
        
        
    #This method generates a computer move with the use of CPU education and advanced machine learning.
    #When this method exits, an 'O' will be placed on the board in a valid (empty) cell.
    @staticmethod
    def makeComputerMove(connectFourBoard):
        validMove = False
        col = -1                
            
        #Keep generating random moves until we find an empty cell to place an 'O'
        while not validMove:
            col = connectFourBoard.computerAttack()
            #placeToken() will return false if the cell is not empty (i.e., we need to try a new spot)
            validMove = connectFourBoard.placeToken(col, 'O')
        

    #This method prompts the user if they would like to play again with some invalidation.
    @staticmethod
    def askPlayAgain():
        #After reading integer values for row/col we need to consume the left-over <return> on the Scanner.
        playAgain = input("Play again? [y/n]: ")
        while (not playAgain == ("y") and not playAgain == ("yes") and not playAgain == ("n") and not playAgain == ("no")):
            playAgain = input("Play again? [y/n]: \n")

        if ((playAgain == ("y")) or (playAgain == ("yes"))):
            return True
        return False

ConnectFour.main()
