import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF

class Flake: # --- This is a record
    def __init__(self,snow_x, snow_y, vel_range, snow_size) -> None:
        self.x = snow_x
        self.y = snow_y
        self.vel = vel_range
        self.size = size
    # --- End fields
# --- End record

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

# --- Number of flakes
snow_rows = 50
snow_arr = [None for j in range(snow_rows)]

for row in range(snow_rows):    
    my_flake = Flake(random.randint(1,width), random.randint(1,height), random.randint(1,3), 5)
    snow_arr[row] = my_flake


# -------- Main Program Loop -----------
while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic should go here
    
    # --- Snow movement
    # if snow_arr[snow_rows][0] <= height:
    #     snow_arr[snow_rows][0] += 1*snow_arr[snow_rows][2]
    # else:
    #     snow_arr[snow_rows][0] = 0
    #     snow_arr[snow_rows][1] = random.randint(1,width)
    for row in range(snow_rows):
        if snow_arr[row].y > size[1]:
            snow_arr[row].y = 0
            snow_arr



    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    pygame.draw.rect(screen, WHITE, [snow_arr.x,snow_arr.y,snow_arr.size,snow_arr.size])

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()