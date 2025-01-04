# Connect Four

This repository contains a Java implementation of the classic Connect Four game. In this game, the user plays against an AI opponent. The AI uses strategic algorithms to challenge the user by attempting to win, block, and make strategic moves.

## Features

- **Interactive Gameplay**: Users can play Connect Four against an AI opponent.
- **AI Strategy**: The AI uses strategic algorithms to make its moves.
- **Simple and Clear Board Representation**: The game board is displayed in the console.

## Requirements

- **Java Development Kit (JDK)**: Ensure you have JDK installed on your machine.

## How to Play

1. **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/ConnectFour.git
    cd ConnectFour
    ```

2. **Compile the Java Files**
    ```sh
    javac Board.java ConnectFour.java
    ```

3. **Run the Game**
    ```sh
    java ConnectFour
    ```

4. **Gameplay Instructions**
    - Enter your name when prompted.
    - Respond "yes" or "no" to start the game.
    - On your turn, input the column number (0-6) where you want to place your token.
    - The AI will then make its move.
    - The game continues until there is a winner or the board is full (tie).

## Code Explanation

### Board.java

- **Class Board**: Models the Connect Four board and includes methods to manipulate the board.
  - **Attributes**:
    - `rows` and `cols`: Define the dimensions of the board.
    - `emptyCells`: Tracks the number of empty cells on the board.
    - `board`: A 2D character array representing the board.
  - **Methods**:
    - `getRows`, `getCols`, `getEmptyCells`: Accessor methods to get the board dimensions and empty cells.
    - `clearBoard`: Initializes the board with empty characters.
    - `printBoard`: Prints the current state of the board.
    - `placeToken`: Places a token on the board if the move is valid.
    - `checkWinner`: Checks if there are four consecutive tokens (horizontally, vertically, or diagonally) for a win.
    - `checkAcross`, `checkVertical`: Helper methods for strategic and winning moves.
    - `computerAttack`: Generates a move for the AI.
    - `toString`: Returns a string representation of the board's statistics.

### ConnectFour.java

- **Class ConnectFour**: Contains the main game loop and handles user and AI moves.
  - **Methods**:
    - `main`: The main game loop that initializes the board and handles user interaction.
    - `makeUserMove`: Prompts the user for a move and validates the input.
    - `makeComputerMove`: Generates and places the AI's move on the board.
    - `askPlayAgain`: Prompts the user if they want to play another round.

## Example

```sh
Welcome to Connect-Four!

What is your name?
> Matt
You ready for a challenge, Matt?
(...YES or NO...)
> yes
Prepare yourself for the greatest match of Connect-Four...

    0   1   2   3   4   5   6  
  -----------------------------
5 |   |   |   |   |   |   |   | 
  -----------------------------
4 |   |   |   |   |   |   |   | 
  -----------------------------
3 |   |   |   |   |   |   |   | 
  -----------------------------
2 |   |   |   |   |   |   |   | 
  -----------------------------
1 |   |   |   |   |   |   |   | 
  -----------------------------
0 |   |   |   |   |   |   |   | 
  -----------------------------
Statistics:
There are: 42 empty cells.
What column would you like to move to (0-6):
> 3
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss potential changes.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was created by Matthew Moga.

