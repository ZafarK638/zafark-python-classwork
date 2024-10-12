import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
width = 1550
height = 800
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
speed = 1

square_width = 15
square_height = 15

x_pos = (width - square_width) // 2  
y_pos = (height - square_height) // 2  

p1_x = 50
p1_y = height/2

p2_x = width - p1_x
p2_y = height/2

paddle_height = 100
paddle_width = 20

move_up_p1 = False
move_down_p1 = False
move_up_p2 = False
move_down_p2 = False

# -------- Main Program Loop -----------
while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        
        if event.type == pygame.KEYDOWN:
            # --- Player 1 controls
            if event.key == pygame.K_w:
                move_up_p1 = True
            if event.key == pygame.K_s:
                move_down_p1 = True
            # --- Player 2 controls
            if event.key == pygame.K_UP:
                move_up_p2 = True
            if event.key == pygame.K_DOWN:
                move_down_p2 = True

        if event.type == pygame.KEYUP:
            # --- Player 1 controls
            if event.key == pygame.K_w:
                move_up_p1 = False
            if event.key == pygame.K_s:
                move_down_p1 = False
            # --- Player 2 controls
            if event.key == pygame.K_UP:
                move_up_p2 = False
            if event.key == pygame.K_DOWN:
                move_down_p2 = False

    # --- Game logic should go here
    multiplier = random.randint(1,3)
    multiplier_s = random.randint(1,3)

    x_pos += speed*velocity_x*multiplier_s
    y_pos += speed*velocity_y*multiplier_s

    # Wall collisions (left and right)
    if x_pos <= 0 or x_pos >= (width - square_width):
        # Reset the ball to the center
        x_pos = (width - square_width) // 2
        y_pos = (height - square_height) // 2
        velocity_x *= -1
        multiplier = 1
        multiplier_s = 1
        

    # Wall collisions (top and bottom)
    if y_pos <= 0 or y_pos >= (height - square_height):
        velocity_y *= -1  # Reverse vertical direction

        if multiplier_s != 1:
            multiplier_s += -1

    # Paddle collisions


    # Check collision with Player 1's paddle
    if p1_x <= x_pos <= (p1_x + paddle_width):
        if p1_y <= y_pos <= (p1_y + paddle_height):
            velocity_x *= -1  # Reverse horizontal direction

            # Calculate the offset from the center of the paddle
            offset = (y_pos - (p1_y + paddle_height / 2)) / (paddle_height / 2)
            # Adjust vertical velocity based on the offset
            velocity_y = offset * multiplier

    # Check collision with Player 2's paddle
    if (p2_x - square_width) <= x_pos <= p2_x:
        if p2_y <= y_pos <= (p2_y + paddle_height):
            velocity_x *= -1  # Reverse horizontal direction
            
            # Calculate the offset from the center of the paddle
            offset = (y_pos - (p2_y + paddle_height / 2)) / (paddle_height / 2)
            # Adjust vertical velocity based on the offset
            velocity_y = offset * multiplier



    # --- Player 1 code
    if move_up_p1:
        if p1_y >= (height-paddle_height):
            p1_y += -3
        elif p1_y <= 0:
            p1_y += 3
        else:
            p1_y += -3


    if move_down_p1:
        if p1_y >= (height-paddle_height):
            p1_y += -3
        elif p1_y <= 0:
            p1_y += 3
        else:
            p1_y += 3

    # --- Player 2 controls
    if move_up_p2:
        if p2_y >= (height-paddle_height):
            p2_y += -3
        elif p2_y <= 0:
            p2_y += 3
        else:
            p2_y += -3


    if move_down_p2:
        if p2_y >= (height-paddle_height):
            p2_y += -3
        elif p2_y <= 0:
            p2_y += 3
        else:
            p2_y += 3

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here

    # --- The bouncy one
    pygame.draw.rect(screen, RED, [x_pos,y_pos,square_width,square_height])

    # --- Player one 
    pygame.draw.rect(screen, BLACK, [p1_x, p1_y, paddle_width, paddle_height])

    # --- Player two
    pygame.draw.rect(screen, BLACK, [p2_x, p2_y, paddle_width, paddle_height])



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 300 frames per second
    clock.tick(300)

# Close the window and quit.
pygame.quit()