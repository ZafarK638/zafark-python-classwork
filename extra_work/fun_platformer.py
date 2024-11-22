import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 800  # Adjusted dimensions for a typical laptop screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Font settings
font = pygame.font.Font(None, 36)

# Player settings
player_size = 25  # Make the player smaller
player_color = RED
player_speed = 7
player_jump = -15
gravity = 1

# Enemy settings
enemy_size = 25  # Make the enemies smaller

# Coin settings
coin_size = 10  # Make the coins smaller

# Level data
initial_levels = [
    {
        "platforms": [
            pygame.Rect(200, HEIGHT - 100, 100, 20),
            pygame.Rect(400, HEIGHT - 200, 100, 20),
            pygame.Rect(600, HEIGHT - 300, 100, 20),
            pygame.Rect(800, HEIGHT - 400, 100, 20),
            pygame.Rect(1000, HEIGHT - 500, 100, 20),
            pygame.Rect(200, HEIGHT - 600, 100, 20),
            pygame.Rect(400, HEIGHT - 700, 100, 20),
            pygame.Rect(600, HEIGHT - 800, 100, 20),
            pygame.Rect(800, HEIGHT - 900, 100, 20),
            pygame.Rect(1000, HEIGHT - 1000, 100, 20)
        ],
        "moving_platforms": [
            {"rect": pygame.Rect(300, HEIGHT - 100, 100, 20), "speed": 2},
            {"rect": pygame.Rect(800, HEIGHT - 400, 100, 20), "speed": 3},
            {"rect": pygame.Rect(500, HEIGHT - 700, 100, 20), "speed": 4}
        ],
        "enemies": [
            {"rect": pygame.Rect(150, HEIGHT - 50, enemy_size, enemy_size), "speed": 3},
            {"rect": pygame.Rect(550, HEIGHT - 150, enemy_size, enemy_size), "speed": 3},
            {"rect": pygame.Rect(750, HEIGHT - 250, enemy_size, enemy_size), "speed": 3},
            {"rect": pygame.Rect(950, HEIGHT - 350, enemy_size, enemy_size), "speed": 3},
            {"rect": pygame.Rect(1150, HEIGHT - 450, enemy_size, enemy_size), "speed": 3}
        ],
        "coins": [
            pygame.Rect(250, HEIGHT - 150, coin_size, coin_size),
            pygame.Rect(450, HEIGHT - 250, coin_size, coin_size),
            pygame.Rect(650, HEIGHT - 350, coin_size, coin_size),
            pygame.Rect(850, HEIGHT - 450, coin_size, coin_size),
            pygame.Rect(1050, HEIGHT - 550, coin_size, coin_size),
            pygame.Rect(1250, HEIGHT - 650, coin_size, coin_size),
            pygame.Rect(1450, HEIGHT - 750, coin_size, coin_size),
            pygame.Rect(1650, HEIGHT - 850, coin_size, coin_size)
        ]
    },
    # Add more levels with increasing difficulty
]

# Deep copy the initial levels to reset them properly
import copy
levels = copy.deepcopy(initial_levels)

# Player starting position
player_x, player_y = WIDTH // 2, HEIGHT - player_size - 10
player_velocity_y = 0
is_jumping = False
score = 0
current_level = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()
fps = 60

# Function to reset the level
def reset_level():
    global player_x, player_y, player_velocity_y, is_jumping, current_level, levels
    current_level = (current_level + 1) % len(levels)
    player_x, player_y = WIDTH // 2, HEIGHT - player_size - 10
    player_velocity_y = 0
    is_jumping = False
    levels = copy.deepcopy(initial_levels)  # Reset the levels

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Keys for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not is_jumping:
        player_velocity_y = player_jump
        is_jumping = True

    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y

    # Prevent player from falling through the ground
    if player_y >= HEIGHT - player_size - 10:
        player_y = HEIGHT - player_size - 10
        player_velocity_y = 0
        is_jumping = False

    # Prevent player from moving off-screen
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_size:
        player_x = WIDTH - player_size

    # Get the current level data
    level_data = levels[current_level]

    # Platform collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for platform in level_data["platforms"]:
        if player_rect.colliderect(platform) and player_velocity_y > 0:
            player_y = platform.y - player_size
            player_velocity_y = 0
            is_jumping = False

    # Moving platforms movement
    for moving_platform in level_data["moving_platforms"]:
        moving_platform["rect"].x += moving_platform["speed"]
        if moving_platform["rect"].right >= WIDTH or moving_platform["rect"].left <= 0:
            moving_platform["speed"] = -moving_platform["speed"]

        # Moving platforms collision detection
        if player_rect.colliderect(moving_platform["rect"]) and player_velocity_y > 0:
            player_y = moving_platform["rect"].y - player_size
            player_velocity_y = 0
            is_jumping = False

    # Enemy movement and collision detection
    for enemy in level_data["enemies"]:
        enemy_rect = enemy["rect"]
        enemy_rect.x += enemy["speed"]
        if enemy_rect.right >= WIDTH or enemy_rect.left <= 0:
            enemy["speed"] = -enemy["speed"]
        if player_rect.colliderect(enemy_rect):
            print("Game Over! Restarting level...")
            player_x, player_y = WIDTH // 2, HEIGHT - player_size - 10
            score = 0
            current_level = 0
            break

    # Coin collection
    for coin in level_data["coins"]:
        if player_rect.colliderect(coin):
            score += 1
            level_data["coins"].remove(coin)

    # Check if all coins are collected to proceed to the next level
    if not level_data["coins"]:
        reset_level()
        continue  # Skip the rest of the loop to load the next level

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, player_color, player_rect)
    for moving_platform in level_data["moving_platforms"]:
        pygame.draw.rect(screen, GREEN, moving_platform["rect"])
    for platform in level_data["platforms"]:
        pygame.draw.rect(screen, GREEN, platform)
    for enemy in level_data["enemies"]:
        pygame.draw.rect(screen, BLUE, enemy["rect"])
    for coin in level_data["coins"]:
        pygame.draw.rect(screen, YELLOW, coin)

    # Display score and level
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {current_level + 1}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    # Update the screen
    pygame.display.flip()
    clock.tick(fps)
