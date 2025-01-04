/**
 * This class models the Connect-four main loop for our game.
 * All in game moves are found here.
 *
 * @author Matthew Moga
 * @version December 14, 2022
 */




import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;




public class ConnectFour {
    
    /**
     * This method defines the mainline logic for our game loop. 
     * It uses a Connect-Four Board object and various helper methods to run the game.
     * 
     * @param args (String[])
     */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Board connectFourBoard = new Board();
        System.out.println("\nWelcome to Connect-Four!\n");
        boolean playGame = false;
        boolean gameLoop = false;
        System.out.println("What is your name?");
        String name = input.nextLine();
        System.out.println("You ready for a challenge, " + name + "?\n(...YES or NO...)");
        String answer = input.nextLine();
        if (answer.equalsIgnoreCase("yes") || (answer.contains("yes"))) {
            System.out.println("Prepare yourself for the greatest match of Connect-Four...");
            playGame = true;
            gameLoop = true;
        }
        else if (answer.equalsIgnoreCase("no") || (answer.contains("no"))) {
            System.out.println("Unfortunate. Practice more and then come back...");
        }
        else {
            System.out.println("Not sure what you mean there, " + name + ". Get serious then come back!!!");
        }
        
        while (gameLoop) {
            playGame = true;
            while (playGame) {
                boolean usersTurn = true;
                connectFourBoard.printBoard();
                System.out.println(connectFourBoard.toString());
                if (usersTurn) {
                    makeUserMove(connectFourBoard, input);
                    makeComputerMove(connectFourBoard);
                }
                usersTurn = !usersTurn;
                if (connectFourBoard.checkWinner('X') == true) {
                    System.out.println("YOU Won!  Congratulations.");
                    playGame = false;
                }
                else if (connectFourBoard.checkWinner('O') == true) {
                    System.out.println("You LOSE!  Heehee!");
                    playGame = false;
                }
                else {
                    if (connectFourBoard.getEmptyCells() == 0) {
                        System.out.println("Tie!  Try harder!");
                        playGame = false;
                    }
                }
            }
            System.out.println("*** G A M E   O V E R ***");
            connectFourBoard.printBoard();
            connectFourBoard.clearBoard();
            gameLoop = askPlayAgain(input);
        }
    }
    
    
    /**
     * This method prompts the user for a move.
     * When this method exits, an 'X' will be placed on the board in a valid (empty) cell.
     *
     * @param connectFourBoardPlayers A Board object for our game.
     * @param input A Scanner object to get user input.
     */
    public static void makeUserMove(Board connectFourBoardPlayers, Scanner input) {
        boolean validMove = false;
        
        // Prompt for a row and column with input validation
        while (!validMove) {
            System.out.print("What column would you like to move to (0-6): ");
            int col = input.nextInt();
            // placeToken() will return false if the col is invalid or the cell is not empty
            validMove = connectFourBoardPlayers.placeToken(col, 'X');
            if (!validMove) {
                System.out.println("Sorry, that location is not available to place an 'X'.");
            }
        }
    }
    
    
    /**
     * This method generates a computer move with the use of CPU education and advanced machine learning.
     * When this method exits, an 'O' will be placed on the board in a valid (empty) cell.
     *
     * @param connectFourBoardPlayers A Board object for our game.
     */
    public static void makeComputerMove(Board connectFourBoardPlayers) {
        Random numberGenerator = new Random();
        boolean validMove = false;
        int col = -1;
        int index;
        
        // Keep generating random moves until we find an empty cell to place an 'O'
        while (!validMove) {
            for (index = 0; index < connectFourBoardPlayers.getRows(); index++) {
                col = (connectFourBoardPlayers.checkAcross(index));
                if (col != -1) break;
            }
            if (col == -1) {
                for (index = 0; index < connectFourBoardPlayers.getCols(); index++) {
                    if (connectFourBoardPlayers.checkVertical(index) == true) {
                        col = index;
                        break;
                    }
                }
            }
            if (col == -1) {
                //col = numberGenerator.nextInt(6);
                col = connectFourBoardPlayers.computerAttack();
                //col = numberGenerator.nextInt(6);
            }
            // placeToken() will return false if the cell is not empty (i.e., we need to try a new spot)
            validMove = connectFourBoardPlayers.placeToken(col, 'O');
        }
    }
    
    
    /**
     * This method prompts the user if they would like to play again with some invalidation.
     * 
     * @param input A Scanner object to get user input.
     * 
     * @return true - If the user like another round
     * @return false - If the user would not like another round
     */
    public static boolean askPlayAgain(Scanner input) {
        // After reading integer values for row/col we need to consume the left-over <return> on the Scanner.
        input.nextLine();
        System.out.println("Play again? [y/n]: ");
        String playAgain = input.nextLine();
        while (!playAgain.equals("y") && !playAgain.equals("yes") && !playAgain.equals("n") && !playAgain.equals("no")) {
            System.out.println("Play again? [y/n]: ");
            playAgain = input.nextLine(); 
        }
        if ((playAgain.equals("y")) || (playAgain.equals("yes"))) {
            return true;
        }
        return false; 
    }
}
