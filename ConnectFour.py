from Board import Board

class ConnectFour:
    def __init__(self):
        pass

    @staticmethod
    def main():
        connectFourBoard = Board()
        print("\nWelcome to Connect-Four!\n")
        gameLoop = False
        name = input("What is your name? ")

        answer = input("\nYou ready for a challenge, " + name + "?\n(...YES or NO...) ").lower()
        if answer == "yes" or answer == "y":
            print("\nPrepare yourself for the greatest match of Connect-Four...\n")
            gameLoop = True
        elif answer == "no" or answer == "n":
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
                if connectFourBoard.checkWinner('X'):
                    print("YOU Won!  Congratulations.\n")
                    playGame = False
                elif connectFourBoard.checkWinner('O'):
                    print("You LOSE!  Heehee!\n")
                    playGame = False
                elif connectFourBoard.getEmptyCells() == 0:
                    print("Tie!  Try harder!\n")
                    playGame = False

            print("*** G A M E   O V E R ***")
            connectFourBoard.printBoard()
            connectFourBoard.clearBoard()
            gameLoop = ConnectFour.askPlayAgain()

    @staticmethod
    def makeUserMove(connectFourBoard):
        validMove = False
        while not validMove:
            try:
                col = int(input("What column would you like to move to (0-6): "))
                if col < 0 or col > 6:
                    raise ValueError("Column out of range.")
                validMove = connectFourBoard.placeToken(col, 'X')
                if not validMove:
                    print("Sorry, that location is not available to place an 'X'.\n")
            except ValueError as e:
                print(f"Invalid input: {e}")

    @staticmethod
    def makeComputerMove(connectFourBoard):
        validMove = False
        while not validMove:
            col = connectFourBoard.computerAttack()
            validMove = connectFourBoard.placeToken(col, 'O')

    @staticmethod
    def askPlayAgain():
        playAgain = input("Play again? [y/n]: ").lower()
        while playAgain not in ("y", "yes", "n", "no"):
            playAgain = input("Play again? [y/n]: \n").lower()
        return playAgain in ("y", "yes")

ConnectFour.main()
