# Quantum Tic-Tac-Toe

An interactive game that teaches quantum computing concepts like superposition and entanglement through a quantum version of Tic-Tac-Toe. This project is built using Python, Pygame, and Qiskit, making it a great educational tool for beginners interested in quantum mechanics and quantum computing.

## Overview

<img width="1365" alt="Screenshot 2025-02-21 at 7 36 13 pm" src="https://github.com/user-attachments/assets/c092ee47-7feb-46f9-8a3b-ab28d64eb9f7" />

### Explanation

#### 1. Graphical Interface (`gui.py`)
- The entry point of the application.
- Handles the graphical user interface using `pygame`.
- Manages user input (e.g., mouse clicks) and renders the game board.

#### 2. Game Moves (`game_logic.py`)
- Contains the core game logic.
- Manages the game state (e.g., the board, player turns).
- Handles moves (classical and quantum) and checks for win conditions.

#### 3. Quantum Moves (`quantum_logic.py`)
- Simulates quantum moves using `qiskit`.
- Generates quantum circuits for superposition and entanglement.
- Displays the quantum circuits in the terminal.

### Flow of the Program

#### 1. User Interaction:
- The user interacts with the game through the GUI (`gui.py`).
- Clicks on the board to make moves.

#### 2. Game Logic:
- `gui.py` calls `game_logic.py` to update the game state and check for valid moves.

#### 3. Quantum Simulation:
- If a quantum move is made, `game_logic.py` calls `quantum_logic.py` to simulate the move using `qiskit`.

#### 4. Visualization:
- `quantum_logic.py` generates and displays the quantum circuit in the terminal.

#### 5. Win Condition:
- After each move, `game_logic.py` checks for a win condition and updates the GUI accordingly.


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
- `qiskit-aer` (for high-performance simulator)
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
pip install pygame qiskit qiskit-aer matplotlib pylatexenc
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
![Screenshot 2025-02-21 020138](https://github.com/user-attachments/assets/7e0057d3-e6ef-4123-8de7-ff0236f70511)

### 2. Quantum (Superposition) Move Visualization:
![Screenshot 2025-02-21 143747](https://github.com/user-attachments/assets/5fe71fc9-4c60-49ef-9ea9-0d42131b2dca)

### 3. Entangled Move Visualization:
![Screenshot 2025-02-21 143753](https://github.com/user-attachments/assets/59e594d4-6323-4858-9f3c-cbbf7c9f85a2)

### 4. Winner Message:
![Screenshot 2025-02-21 020202](https://github.com/user-attachments/assets/ab5ba301-1d86-413a-9f15-ed728013c5cc)

![Screenshot 2025-02-21 145301](https://github.com/user-attachments/assets/a194dbac-3c9a-4285-beff-b2af599e7053)

### 5. Example of Playing the Game:


https://github.com/user-attachments/assets/3f019296-a47d-4642-aecc-0c55893c50a9

## Quantum Moves Further Explained

### Quantum (Superposition) Moves
- When a player makes a quantum move, the `apply_superposition()` function generates the circuit and displays it on the terminal.
- The qubit is measured, and the result (`X` or `O`) is placed on the board.
- Below is the quantum circuit for a single-qubit superposition. <br>
![Screenshot 2025-02-21 143747](https://github.com/user-attachments/assets/5fe71fc9-4c60-49ef-9ea9-0d42131b2dca)
- **Explanation**:
  - `q0`: The qubit starts in the state |0⟩.
  - `H`: The Hadamard gate is applied to `q0`, creating a superposition.
  - `M`: The qubit is measured, and the result is stored in the classical bit `c0`.
- **Circuit Description**:
  - **Qubit (`q0`)**: The circuit has one qubit (`q0`) and one classical bit (`c0`).
  - **Hadamard Gate (`H`)**:
    - The Hadamard gate is applied to `q0`, creating a superposition state.
    - Mathematically, the Hadamard gate transforms the qubit state as follows.
    - This means the qubit is in an equal superposition of `|0⟩` and `|1⟩`.

$$ H∣0⟩ = {{∣0⟩ + ∣1⟩} \over \sqrt2} , H∣1⟩ = {{∣0⟩ - ∣1⟩} \over \sqrt2} $$

  - **Measurement (`M`)**:
    - After applying the Hadamard gate, the qubit is measured.
    - The measurement collapses the superposition into either `|0⟩` or `|1⟩`, and the result is stored in the classical bit `c0`.
- **Summary**:
  - Represents a single-qubit superposition.
  - Applies a Hadamard gate to create a superposition and measures the result.
  - Used for quantum moves in the game.

### Entanglement Moves
- In quantum mechanics, entanglement is a phenomenon where two or more particles become linked, and the state of one particle instantly influences the state of the other, no matter the distance between them.
- In your game, when you make an entangled move, two cells are linked together. The result of the quantum measurement (collapse) affects both cells simultaneously.
- When you click an empty cell, the `apply_entanglement()` function in `quantum_logic.py` is called.
- This function creates a quantum circuit with two qubits, entangles them, and measures their states.
- The measurement result (e.g., `00`, `01`, `10`, or `11`) determines the marks (`X` or `O`) for both cells.
- Below is the quantum circuit for two-qubit entanglement. <br>
![Screenshot 2025-02-21 143753](https://github.com/user-attachments/assets/59e594d4-6323-4858-9f3c-cbbf7c9f85a2)
- **Explanation**:
  - `q0`: The first qubit starts in the state `|0⟩`.
  - `H`: The Hadamard gate is applied to `q0`, creating a superposition.
  - `■`: The CNOT gate is applied with `q0` as the control qubit and `q1` as the target qubit.
  - `X`: The target qubit (`q1`) is flipped if the control qubit (`q0`) is |`1`⟩.
  - `M`: Both qubits are measured, and the results are stored in the classical bits `c0` and `c1`.
- **Circuit Description**:
  - **Qubits (`q0` and `q1`)**: The circuit has two qubits (`q0` and `q1`) and two classical bits (`c0` and `c1`).
  - **Hadamard Gate (`H`) on `q0`**:
    - The Hadamard gate is applied to `q0`, creating a superposition state.
  - **CNOT Gate (`CX`)**:
    - The CNOT gate is applied with `q0` as the control qubit and `q1` as the target qubit.
    - This gate entangles the two qubits, creating a Bell state.
    - The state of `q1` depends on the state of `q0`.

$$ ∣\Phi^+⟩ = {{∣00⟩ + ∣11⟩} \over \sqrt2} $$

  - **Measurements (M)**:
    - Both qubits are measured, and the results are stored in the classical bits `c0` and `c1`.
- **Summary**:
  - Represents a two-qubit entanglement.
  - Applies a Hadamard gate to the first qubit and a CNOT gate to entangle the two qubits.
  - Used for entangled moves in the game.

## Project Structure
```
QuantumTicTacToe/
├── gui.py                # Main GUI script using pygame
├── game_logic.py         # Game logic and rules
├── quantum_logic.py      # Quantum simulation and circuit generation
└── README.md             # Project documentation
```
## License

This project is open-source under the MIT License.
