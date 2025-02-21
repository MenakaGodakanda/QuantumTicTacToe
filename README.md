# Quantum Tic-Tac-Toe

An interactive game that teaches quantum computing concepts like superposition and entanglement through a quantum version of Tic-Tac-Toe. This project is built using Python, Pygame, and Qiskit, making it a great educational tool for beginners interested in quantum mechanics and quantum computing.

<img width="999" alt="Screenshot 2025-02-21 at 2 43 25 pm" src="https://github.com/user-attachments/assets/07175f2c-8f3d-4e9a-ab08-b1f73fd1f97d" />

## Overview
### 1. Graphical Interface (`gui.py`)
- Uses Pygame to render the board and handle player interactions.
- Captures player moves and sends them to game_logic.py.

### 2. Game Moves (`game_logic.py`)
- Processes player moves and validates the board state.
- Decides when to invoke quantum logic for superposition or entanglement.

### 3. Quantum Moves (`quantum_logic.py`)
- Uses Qiskit to simulate quantum behavior.
- Implements quantum mechanics like superposition and entanglement.

## Features

- **Classic Tic-Tac-Toe**: Play the traditional 3x3 Tic-Tac-Toe game.
- **Quantum Moves**: Use quantum superposition to place a move that can collapse into either `X` or `O`.
- **Entanglement**: Create entangled moves that affect multiple cells simultaneously.
- **Interactive GUI**: Built with pygame for an engaging user experience.
- **Quantum Circuit Visualization**: View the quantum circuit used for each move directly in the terminal.

## Requirements
To run this project, you need the following Python libraries:
- `pygame` (for the GUI)
- `qiskit` (for quantum simulation)
- `matplotlib` (for quantum circuit visualization)
- `pylatexenc` (for rendering LaTeX in quantum circuit diagrams)

## Installation & Setup

### Step 1: Clone the Repository
```
git clone https://github.com/MenakaGodakanda/QuantumTicTacToe.git
cd QuantumTicTacToe
```

### Step 2: Set Up a Virtual Environment
```
python3 -m venv tictactoe
source tictactoe/bin/activate  # (Linux/macOS)
# For Windows: tictactoe\Scripts\activate
```

### Step 3: Install Dependencies
```
pip install pygame qiskit matplotlib pylatexenc
```

### Step 4: Run the Game
```
python3 gui.py
```

## How to Play
### 1. Launch the Game:
- Run `python3 gui.py` to start the game.
- A 3x3 grid will appear on the screen.

### 2. Make a Move:
- Click on an empty cell to place a move.
- If you want to make a quantum move, the game will simulate a quantum superposition and collapse it into either `X` or `O`.
- If you want to make an entangled move, the game will simulate entanglement and place marks in two cells simultaneously.

### 3. Winning the Game:
- The game follows the classic Tic-Tac-Toe rules. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.

### 4. Quantum Features:
- Quantum moves are visualized using quantum circuits, which are displayed in the terminal.

## Screenshots

### 1. Game Board:

### 2. Quantum Move Visualization:

### 3. Entangled Move Visualization:

### 4. Winner Message:

### 5. Example of Playing the Game:


## Project Structure
```
QuantumTicTacToe/
├── gui.py                # Main GUI script using pygame
├── game_logic.py         # Game logic and rules
├── quantum_logic.py      # Quantum simulation and circuit generation
├── README.md             # Project documentation
├── quantum_move.png      # Example quantum circuit visualization
└── entanglement.png      # Example entangled circuit visualization
```
## License

This project is open-source under the MIT License.
