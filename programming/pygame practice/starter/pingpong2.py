import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
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
player_size = 50
player_color = RED
player_speed = 7
player_jump = -15
gravity = 1

# Enemy settings
enemy_size = 50
enemy_speed = 3

# Coin settings
coin_size = 20

# Level data
levels = [
    {
        "platforms": [
            pygame.Rect(200, 500, 100, 20),
            pygame.Rect(400, 400, 100, 20),
            pygame.Rect(600, 300, 100, 20),
            pygame.Rect(100, 200, 100, 20)
        ],
        "moving_platform": pygame.Rect(300, 200, 100, 20),
        "enemies": [
            pygame.Rect(150, 550, enemy_size, enemy_size),
            pygame.Rect(550, 450, enemy_size, enemy_size)
        ],
        "coins": [
            pygame.Rect(250, 450, coin_size, coin_size),
            pygame.Rect(450, 350, coin_size, coin_size),
            pygame.Rect(650, 250, coin_size, coin_size)
        ]
    },
    # Add more levels with increasing difficulty
]

# Player starting position
player_x, player_y = WIDTH // 2, HEIGHT - player_size - 10
player_velocity_y = 0
is_jumping = False
score = 0
current_level = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()
fps = 60

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

    # Moving platform movement
    moving_platform = level_data["moving_platform"]
    moving_platform.x += enemy_speed
    if moving_platform.right >= WIDTH or moving_platform.left <= 0:
        enemy_speed = -enemy_speed

    # Moving platform collision detection
    if player_rect.colliderect(moving_platform) and player_velocity_y > 0:
        player_y = moving_platform.y - player_size
        player_velocity_y = 0
        is_jumping = False

    # Enemy movement and collision detection
    for enemy in level_data["enemies"]:
        enemy.x += enemy_speed
        if enemy.right >= WIDTH or enemy.left <= 0:
            enemy_speed = -enemy_speed
        if player_rect.colliderect(enemy):
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

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, player_color, player_rect)
    pygame.draw.rect(screen, GREEN, moving_platform)
    for platform in level_data["platforms"]:
        pygame.draw.rect(screen, GREEN, platform)
    for enemy in level_data["enemies"]:
        pygame.draw.rect(screen, BLUE, enemy)
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

    # Check if all coins are collected to proceed to the next level
    if not level_data["coins"]:
        current_level = (current_level + 1) % len(levels)
        player_x, player_y = WIDTH // 2, HEIGHT - player_size - 10
        player_velocity_y = 0
        is_jumping = False
