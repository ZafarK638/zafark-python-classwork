import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF

class Flake: # --- This is a class
    def __init__(self) -> None:
        self.x = random.randint(1,width)
        self.y = random.randint(1,height)
        self.vel = random.randint(1,3)
        self.size = 5-self.size
    # --- End fields

    def fall(self):
        if self.y > height[i]:
            self.y > 0
            self.x = random.randint(0,width[0]-1)
        else:
            self.y = 0
            self.x = random.randint(1,width[0]-1)

    def draw(self):
        pygame.draw.rect(screen, WHITE, [self.x,self.y,self.size,self.size])


# --- End record

pygame.init()

# Set the width and height of the screen [width, height]
width = 1000
height = 700
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


# Loop until the user clicks the close button.
gameOver = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# --- Number of flakes
number_of_flakes = 500
flakes = [None for j in range(number_of_flakes)]

for row in range(number_of_flakes):    
    my_flake = flakes
    number_of_flakes[row] = my_flake


# -------- Main Program Loop -----------
while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic should go here
    # --- Snow movement
    for i in range(number_of_flakes):
        i.fall



    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    for i in flakes:
        flakes.draw

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()