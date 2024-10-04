import pygame
import math

# Define some colors
BLACK    = (0,0,0)
WHITE    = (255,255,255)
GREEN    = (0,255,0)
RED      = (255,0,0)
BLUE     = (0,0,255)

pygame.init

PI = math.pi

size = (1500,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kabir's Crackalackin' Game")

# Loop until the user clicks the close button.
gameOver = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
#main_program_loop
while not gameOver:
    #main_event_loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            gameOver = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
    # --- Game logic should go here


    # --- Drawing code should go here
    

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit