# Connect Four

This is a Python implementation of the classic Connect Four game. Users can play against a computer opponent with the ability to place tokens on the board, and the game logic ensures that the computer makes strategic moves to provide a challenging experience.

## Features

- **Interactive Gameplay**: Users can play Connect Four against a computer opponent.
- **Board Management**: The board is managed using a 2D array, with methods to place tokens, check for winners, and clear the board.
- **Input Validation**: Ensures that all user inputs are valid and within expected ranges.
- **Computer Strategy**: The computer uses a set of heuristics to make strategic moves.
- **Game Status**: Displays the current state of the board and game statistics.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/username/connect-four.git
    cd connect-four
    ```

2. **Run the game**:
    ```bash
    python ConnectFour.py
    ```

## Usage

1. **Start the game**:
    - Run the `ConnectFour.py` script.
    - Follow the prompts to start the game.

2. **Gameplay**:
    - Users will be prompted to enter their name and whether they are ready to play.
    - The game alternates turns between the user and the computer.
    - The user is prompted to select a column (0-6) to place their token.
    - The game checks for winning conditions after each move.

3. **End of Game**:
    - The game announces the winner or if there is a tie.
    - Users are prompted to play again or exit.

## Example

Here is an example interaction with the game:
