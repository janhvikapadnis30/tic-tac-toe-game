# XO Tic-Tac-Toe Game

A modular and interactive command-line Tic-Tac-Toe game developed using Python. The project supports both local two-player gameplay and single-player gameplay against an AI opponent. It includes input validation, win/draw detection, score tracking, and unit testing.

## Features

* **Single-Player Mode:** Play against an AI opponent using decision-making logic.
* **Two-Player Mode:** Play locally with another player on the same computer.
* **Input Validation:** Prevents invalid, non-numeric, out-of-range, and already occupied moves.
* **Dynamic Board Display:** Displays the 3×3 game board after every move.
* **Win and Draw Detection:** Automatically checks rows, columns, and diagonals for winning conditions and detects draws.
* **Score Tracking:** Maintains game scores across multiple rounds.
* **Modular Design:** Game functionality is separated into different Python modules.
* **Unit Testing:** Includes tests for important game components.

## Technologies Used

* **Programming Language:** Python 3.x
* **Version Control:** Git and GitHub
* **Testing:** Python unit testing
* **Storage:** Local file storage for score information
* **External Packages:** No external Python packages are required.

## Project Structure

```text
tic-tac-toe-game/
│
├── main.py
├── board.py
├── game_engine.py
├── ai_engine.py
├── score_tracker.py
├── validator.py
│
├── tests/
│   ├── test_board.py
│   └── test_ai.py
│
├── statement.md
├── README.md
└── .gitignore
```

## Requirements

* Python 3.x
* Git (optional, if cloning the repository)

No external Python packages are required.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/janhvikapadnis30/tic-tac-toe-game.git
```

2. Open the project folder:

```bash
cd tic-tac-toe-game
```

## How to Run

Run the main program using:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

## How to Play

1. The game is played on a 3×3 board.
2. Select the required game mode.
3. Player 1 uses **X**.
4. Player 2 or the AI uses **O**.
5. Enter the number corresponding to the board position where you want to place your mark.
6. A player wins by placing three marks in a row horizontally, vertically, or diagonally.
7. If all nine positions are filled without a winner, the game ends in a draw.
8. Invalid or occupied positions are rejected and the player is asked to enter another valid move.

## Testing

The project includes unit tests for important game components.

Run the tests using:

```bash
python -m unittest discover
```

The test files are located in the `tests/` directory.

## Functional Modules

The project is divided into the following major functional modules:

1. **Board Module** – Manages the game board and board operations.
2. **Game Engine Module** – Controls turns, game flow, and winning/draw conditions.
3. **AI Engine Module** – Handles the computer opponent's decision-making.
4. **Score Tracker Module** – Maintains scores and game results.
5. **Validator Module** – Validates player input and prevents invalid moves.

## Non-Functional Requirements

### 1. Usability

The game provides simple command-line interaction and clear instructions for players.

### 2. Reliability

The application validates user input and prevents invalid moves from interrupting normal gameplay.

### 3. Maintainability

The application follows a modular structure where different responsibilities are separated into individual Python files.

### 4. Performance

The game performs board operations, validation, and win-condition checks efficiently for a 3×3 board.

### 5. Error Handling

Invalid, non-numeric, out-of-range, and occupied-position inputs are handled without terminating the game unexpectedly.

## Author

**Janhvi Kapadnis**

GitHub: [janhvikapadnis30](https://github.com/janhvikapadnis30)
