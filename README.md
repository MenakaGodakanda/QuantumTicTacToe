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
├── README.md             # Project documentation
├── quantum_move.png      # Example quantum circuit visualization
└── entanglement.png      # Example entangled circuit visualization
```
## License

This project is open-source under the MIT License.
