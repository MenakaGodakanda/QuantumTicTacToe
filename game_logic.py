class QuantumTicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def make_move(self, row, col, quantum=False, entangled=False):
        """Handles move placement and quantum logic"""
        from quantum_logic import apply_superposition, apply_entanglement
        
        if self.board[row][col] == ' ':
            if quantum:
                if entangled:
                    result = apply_entanglement()  # Call apply_entanglement for entangled moves
                    self.board[row][col] = result[0]
                    # Place the second result in another cell (for simplicity)
                    next_row, next_col = (row, col + 1) if col < 2 else (row + 1, 0)
                    if next_row < 3 and next_col < 3:
                        self.board[next_row][next_col] = result[1]
                else:
                    self.board[row][col] = apply_superposition()  # Call apply_superposition for quantum moves
            else:
                self.board[row][col] = self.current_player  # Classical move
            self.switch_player()
            return True
        return False
    
    def switch_player(self):
        """Switches turn between X and O"""
        self.current_player = 'X' if self.current_player == 'O' else 'O'

    def check_winner(self):
        """Check for a winner in the board"""
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]
        return None

    def print_board(self):
        """Prints the board"""
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
