# Quantum Tic-Tac-Toe

An interactive game that teaches quantum computing concepts like superposition and entanglement through a quantum version of Tic-Tac-Toe. This project is built using Python, Pygame, and Qiskit, making it a great educational tool for beginners interested in quantum mechanics and quantum computing.

## Features

- Quantum Moves – Players can place superpositioned moves.
- Quantum Entanglement – Positions can be entangled for advanced gameplay.
- Graphical UI – Built using Pygame for an interactive experience.
- Quantum Circuit Visualization – Uses Qiskit to simulate quantum moves.
- Quantum Move Animations – Dynamic visualization of quantum effects.

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

### 3. Winning the Game:
- The game follows the classic Tic-Tac-Toe rules. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.

### 4. Quantum Features:
- Quantum moves are visualized using quantum circuits, which are saved as images (`quantum_move.png` and `entanglement.png`).

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
