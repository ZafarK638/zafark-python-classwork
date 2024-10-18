import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF

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

# --- Number of flakes
snow_rows = 500
snow_arr = [None for j in range(snow_rows)]

for row in range(snow_rows):    
    flake_speed = random.randint(1,3)
    flake_size = 5-(flake_speed)
    my_flake = Flake(random.randint(1,width), random.randint(1,height), flake_speed, flake_size)
    snow_arr[row] = my_flake


# -------- Main Program Loop -----------
while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic should go here
    # --- Snow movement
    for i in range(snow_rows):
        if snow_arr[i].y <= height:
            snow_arr[i].y += 1*snow_arr[i].vel
        else:
            snow_arr[i].y = 0
            snow_arr[i].x = random.randint(1,width)



    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    for i in range(snow_rows):
        pygame.draw.rect(screen, WHITE, [snow_arr[i].x,snow_arr[i].y,snow_arr[i].size,snow_arr[i].size])

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()