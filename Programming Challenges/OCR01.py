import pygame
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

pygame.init()

# Set the width and height of the screen [width, height]
width = 700
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Factorial Calculator")

# Fonts
font = pygame.font.Font(None, 36)
input_font = pygame.font.Font(None, 48)
title_font = pygame.font.Font(None, 64)

# Input and output variables
input_text = ""
result_text = ""

# Function to calculate factorial using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Function to calculate factorial using a loop
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function to wrap text to fit within a certain width
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

# Main Program Loop
gameOver = False
clock = pygame.time.Clock()

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Calculate factorial
                try:
                    num = int(input_text)
                    if num < 0:
                        result_text = "Enter a non-negative integer."
                    else:
                        # Choose between recursive or loop-based calculation
                        result_text = f"Factorial: {factorial_recursive(num)}"
                except ValueError:
                    result_text = "Invalid input! Enter a number."
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Clear the screen with a gradient background
    for y in range(height):
        color = (LIGHT_GRAY[0] - y // 10, LIGHT_GRAY[1] - y // 10, LIGHT_GRAY[2] - y // 10)
        pygame.draw.line(screen, color, (0, y), (width, y))

    # Draw title
    title_surface = title_font.render("Factorial Calculator", True, BLUE)
    screen.blit(title_surface, (width // 2 - title_surface.get_width() // 2, 20))

    # Render input box
    input_box = pygame.Rect(150, 150, 400, 50)
    pygame.draw.rect(screen, DARK_GRAY, input_box)
    pygame.draw.rect(screen, BLACK, input_box, 2)

    # Render text
    input_surface = input_font.render(input_text, True, WHITE)
    wrapped_result = wrap_text(result_text, font, 500)

    # Blit text and input box
    screen.blit(input_surface, (input_box.x + 10, input_box.y + 10))
    for i, line in enumerate(wrapped_result):
        result_surface = font.render(line, True, GREEN if result_text.startswith("Factorial") else RED)
        screen.blit(result_surface, (150, 250 + i * 30))

    # Instructions
    instructions = wrap_text("Enter a number and press Enter to calculate its factorial.", font, 600)
    for i, line in enumerate(instructions):
        instruction_surface = font.render(line, True, BLACK)
        screen.blit(instruction_surface, (50, 100 + i * 30))

    # Update the screen
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
sys.exit()
