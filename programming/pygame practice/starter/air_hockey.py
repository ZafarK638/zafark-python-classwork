import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
width = 700
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Air Hockey")

# Loop until the user clicks the close button.
gameOver = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
x_pos = 0
y_pos = 0
velocity_x = 1
velocity_y = 1
square_width = 50
square_height = 50

# -------- Main Program Loop -----------
while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic should go here

    if x_pos > (width-square_width):
        x_pos += -1
        velocity_x *= -1
    elif x_pos < 0: 
        x_pos += 1
        velocity_x *= -1
    else: 
        x_pos += 1 * (int(velocity_x))



    if y_pos > (height-square_height):
        y_pos += -1
        velocity_y *= -1
    elif y_pos < 0:
        y_pos += 1
        velocity_y *= -1
    else: 
        y_pos += 1 * (int(velocity_y))


    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)

    # --- Drawing code should go here

    pygame.draw.rect(screen, RED, [x_pos,y_pos,square_width,square_height])



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()