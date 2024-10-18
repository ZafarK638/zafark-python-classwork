import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF



pygame.init()

# Set the width and height of the screen [width, height]
width = 700
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


# Loop until the user clicks the close button.
gameOver = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# --- Snow position
snow_x = random.randint(1,width)
snow_y = random.randint(1,height)

# --- Snow speed
snow_velocity = 3

# --- Snow size
snow_width = 5
snow_height = 5

# --- Number of flakes


# -------- Main Program Loop -----------
while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic should go here
    
    # --- Snow movement
    if snow_y <= height:
        snow_y += 1*snow_velocity
    else:
        snow_y = 0
        snow_x = random.randint(1,width)



    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    pygame.draw.rect(screen, WHITE, [snow_x,snow_y,snow_width,snow_height])

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()