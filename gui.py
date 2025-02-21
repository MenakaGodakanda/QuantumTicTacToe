import pygame
import time
from game_logic import QuantumTicTacToe
from quantum_logic import apply_superposition, apply_entanglement

pygame.init()

WIDTH, HEIGHT = 300, 300
WHITE, BLACK, BLUE, RED, GREEN = (255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quantum Tic-Tac-Toe")

font = pygame.font.Font(None, 40)
game = QuantumTicTacToe()

def draw_board():
    """Draws the Tic-Tac-Toe grid"""
    screen.fill(WHITE)
    for x in range(1, 3):
        pygame.draw.line(screen, BLACK, (x * 100, 0), (x * 100, HEIGHT), 2)
        pygame.draw.line(screen, BLACK, (0, x * 100), (WIDTH, x * 100), 2)

def draw_marks():
    """Draws the marks on the board"""
    for row in range(3):
        for col in range(3):
            mark = game.board[row][col]
            if mark != ' ':
                text = font.render(mark, True, BLUE)
                screen.blit(text, (col * 100 + 40, row * 100 + 30))

def animate_superposition(row, col):
    """Animates a quantum move using blinking effect"""
    for _ in range(5):  # Blink effect
        pygame.draw.rect(screen, WHITE, (col * 100, row * 100, 100, 100))
        pygame.display.flip()
        time.sleep(0.2)
        
        text = font.render("?", True, RED)
        screen.blit(text, (col * 100 + 40, row * 100 + 30))
        pygame.display.flip()
        time.sleep(0.2)

running = True
game_over = False  # Track if the game is over
winner = None  # Track the winner

while running:
    screen.fill(WHITE)
    draw_board()
    draw_marks()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit event detected. Exiting game loop.")
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            row, col = y // 100, x // 100
            if game.board[row][col] == ' ':
                animate_superposition(row, col)  # Show animation
                # Toggle between quantum and entangled moves
                if (row + col) % 2 == 0:  # Example condition for entangled moves
                    game.make_move(row, col, quantum=True, entangled=True)  # Assign entangled move
                else:
                    game.make_move(row, col, quantum=True, entangled=False)  # Assign quantum move
                winner = game.check_winner()
                if winner:
                    print(f"Player {winner} wins!")
                    game_over = True  # Set game over flag

    # If the game is over, display the winner message
    if game_over:
        # Create a surface for the winner message with a background color
        winner_text = font.render(f"Player {winner} wins!", True, WHITE)  # White text
        text_width, text_height = winner_text.get_size()
        background = pygame.Surface((text_width + 20, text_height + 20))  # Add padding
        background.fill(GREEN)  # Green background
        background.blit(winner_text, (10, 10))  # Center the text

        # Display the background and text on the screen
        screen.blit(background, (WIDTH // 2 - (text_width + 20) // 2, HEIGHT // 2 - (text_height + 20) // 2))
        pygame.display.flip()

        # Wait for 3 seconds before closing the window
        time.sleep(3)
        running = False

# Clean up Pygame resources
print("Cleaning up Pygame resources...")
pygame.quit()  # Quit Pygame
print("Pygame resources cleaned up. Exiting program.")
