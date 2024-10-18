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
        self.size = snow_size
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
    speed = random.randint(1,3)
    size =10-(speed*2)
    my_flake = Flake(random.randint(1,width), random.randint(1,height), speed, size)
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