import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Invader: # --- This is a record
    def __init__(self,inv_x, inv_y, inv_vel, inv_size) -> None:
        self.x = inv_x
        self.y = inv_y
        self.vel = inv_vel
        self.size = inv_size
    # --- End fields
# --- End record

pygame.init()

# Set the width and height of the screen [width, height]
width = 1000
height = 700
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Invaders")


# Loop until the user clicks the close button.
gameOver = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# --- Number of Invaders
inv_rows = 50
inv_arr = [None for j in range(inv_rows)]

for row in range(inv_rows):    
    # --- Change the random values to be the positions of the invaders
    invaders = Invader(random.randint(1,width), random.randint(1,height), 3, 10)
    inv_arr[row] = invaders


# -------- Main Program Loop -----------
while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic should go here
    # --- Invader movement


    # --- Change this to be the motion of the invaders
    for i in range(inv_rows):
        if inv_arr[i].y <= height:
            inv_arr[i].y += 1*inv_arr[i].vel
        else:
            inv_arr[i].y = 0
            inv_arr[i].x = random.randint(1,width)



    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    for i in range(inv_rows):
        pygame.draw.rect(screen, RED, [inv_arr[i].x,inv_arr[i].y,inv_arr[i].size,inv_arr[i].size])

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()