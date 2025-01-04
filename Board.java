/**
 * This class models the Connect-four board for our game.
 * All methods required to manipulate the board are found here.
 *
 * @author Matthew Moga
 * @version January 5, 2024
 */




import java.util.Arrays;
import java.util.Random;
public class Board {
    
    
    // Properly encapsulated (private) instance variables
    private int rows = 6;
    private int cols = 7;
    private int emptyCells = rows * cols;
    
    
    /**
     * This accessor returns the number of rows on the board.
     *
     * @return int - rows
     */
    public int getRows() {
        return rows;
    }
    
    
    /**
     * This accessor returns the number of columns on the board.
     *
     * @return int - cols
     */
    public int getCols() {
        return cols;
    }
    
    
    /**
     * This accessor returns the number of free cells left on the board.
     *
     * @return int - emptyCells
     */
    public int getEmptyCells() {
        return emptyCells;
    }
    
    
    // Design Decision: I will represent the Board using an array of char(acters) rather than Strings.
    // Since char is a primitive data type it uses less memory and we can use == for comparisons.
    private char[][] board = new char[rows][cols];
    
    
    /**
     * This no-argument constructor initializes all instance variables.
     */
    public Board() {
        clearBoard();
    }
    
    
    /**
     * This mutator initializes all board indices with empty characters.
     */
    public void clearBoard() {
        // Fill the board with blank spaces
        emptyCells = rows * cols;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                board[row][col] = ' ';
            }
        }
    }
    
    
    /**
     * This method will print a Connect-Four board.
     * This method has no parameters and returns nothing.
     */
    public void printBoard() {
        System.out.println("    0   1   2   3   4   5   6  ");
        System.out.println("  -----------------------------");
        for (int i = 0; i < rows; i++) {
            System.out.printf("%s ", rows - i - 1);
            for (int j = 0; j < 2 * cols + 1; j++) {
                if ((j % 2) == 0) {
                    System.out.print('|');
                }
                else System.out.print(board[rows - i - 1][j / 2]);
                System.out.print(' ');
            }
            System.out.print('\n');
            System.out.println("  -----------------------------");
        }
    }
    
    
    /**
     * This method attempts to place a given player token on the board.  
     * It checks that the given row and col are valid indices and also that the chosen cell is ' ' empty.
     * If so, it places the given token in that cell, and returns true.
     * Otherwise, it does not change the board and returns false.
     *
     * @param col (int)
     * @param token (char)
     *
     * @return true - If the location was valid and empty
     * @return false - If the location was invalid and filled
     */
    public boolean placeToken(int col, char token) {
        // Check that the row is in range (0..6) and the cell is empty before allowing the move
        for (int row = 0; row < getRows(); row++) {
            if ( 0 <= col && col < cols && board[row][col] == ' ') {
                board[row][col] = token;
                emptyCells--;
                return true;
            }
        }
        // Invalid move, row is out of range (0..6) or the cell was not empty
        return false;
    }
    
    
    /**
     * This method checks if there are 4 'X' or 4 'O' characters in a row (vertically, horizontally, or diagonally) on the board.
     *
     * @param playerSymbol (char)
     * 
     * @return true - If there are 4 X's in a row or 4 O's in a row
     * @return false - If there is a tie between the player and the computer
     */
    public boolean checkWinner(char playerSymbol) {
        //check for 4 across
        for(int row = 0; row < getRows(); row++) {
            for (int col = 0; col < board[0].length - 3; col++) {
                if ((board[row][col] == playerSymbol) &&
                    (board[row][col+1] == playerSymbol) &&
                    (board[row][col+2] == playerSymbol) &&
                    (board[row][col+3] == playerSymbol)) {
                    return true;
                }
            }
        }
        //check for 4 up and down
        for(int row = 0; row < getRows() - 3; row++) {
            for(int col = 0; col < board[0].length; col++) {
                if ((board[row][col] == playerSymbol) &&
                    (board[row+1][col] == playerSymbol) &&
                    (board[row+2][col] == playerSymbol) &&
                    (board[row+3][col] == playerSymbol)) {
                    return true;
                }
            }
        }
        //check upward diagonal
        for(int row = 3; row < getRows(); row++){
            for(int col = 0; col < board[0].length - 3; col++) {
                if ((board[row][col] == playerSymbol) &&
                    (board[row-1][col+1] == playerSymbol) &&
                    (board[row-2][col+2] == playerSymbol) &&
                    (board[row-3][col+3] == playerSymbol)) {
                    return true;
                }
            }
        }
        //check downward diagonal
        for(int row = 0; row < getRows() - 3; row++) {
            for(int col = 0; col < board[0].length - 3; col++) {
                if ((board[row][col] == playerSymbol) &&
                    (board[row+1][col+1] == playerSymbol) &&
                    (board[row+2][col+2] == playerSymbol) &&
                    (board[row+3][col+3] == playerSymbol)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    
    /**
     * This method checks if there are 2 'X' characters in a row, horizontally on the board.
     *
     * @param row (int)
     * 
     * @return col + 2 - If there are 2 X's in a row horizontally and an empty character (' ')
     * @return col - If there is an empty character (' '), proceeding with two X's horizontally
     */
    public int checkAcross(int row) {
        for (int col = 0; col < getCols() - 2; col++) {
            if (((board[row][col] == 'X') && (board[row][col + 1] == 'X') && (board[row][col + 2] == ' '))) {
                return col + 2;
            }
            else if (((board[row][col] == ' ') && (board[row][col + 1] == 'X') && (board[row][col + 2] == 'X'))) {
                return col;
            }
        }
        return -1;
    }


    
    /**
     * This method checks if there are 2 'X' characters in a row or 3, vertically on the board.
     *
     * @param col (int)
     * 
     * @return true - If there are 2 or 3 X's in a row vertically and an empty character (' ')
     */
    public boolean checkVertical(int col) {
        for (int row = 0; row < getRows() - 3; row++) {
            if (((board[row][col] == 'X') && (board[row+1][col] == 'X') && (board[row + 2][col] == 'X') && (board[row + 3][col] == ' '))) {
                return true;
            }
        }
        for (int row = 0; row < getRows() - 2; row++) {
            if (((board[row][col] == 'X') && (board[row+1][col] == 'X') && (board[row + 2][col] == ' '))) {
                return true;
            }
        }
        return false;
    } 
    
    
    /**
     * This method checks if there is a singular 'O' character, horizontally on the board.
     *
     * @return col + 1 - If there are is an O and an empty character (' ') adjacent to each other
     * @return col - If inner loop is not executed
     */
    public int computerAttack() {
        int row = 0;
        int col = 0;
        for (row = 0; row < getRows() - 1; row++) {
            for (col = 0; col < getCols() - 1; col++) {
                if (((board[row][col]) == 'O' && (board[row][col + 1]) == ' ' )) {
                    return col + 1;
                }
                else {
                    Random numberGenerator = new Random();
                    col = numberGenerator.nextInt(6);
                    // Initially, there was a bug in main where I dropped all the pieces down to column 6
                    // Once this column was filled, I could not place a piece anywhere else on the board
                    return col;
                }
            }
        }
        return col;
    }
     
    
    /**
     * Standard toString method.
     *
     * @return String representation of the current statistics in the Connect-Four battle
     */
    @Override
    public String toString() {
        return "Statistics: \n" + "There are: " + getEmptyCells() + " empty cells.";
    }
}
