import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
width = 1000
height = 700
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
square_width = 15
square_height = 15

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



    # --- Player 1 code
    if move_up_p1:
        if p1_y >= (height-paddle_height):
            p1_y += -3
        elif p1_y <= paddle_height:
            p1_y += 3
        else:
            p1_y += -3


    if move_down_p1:
        if p1_y >= (height-paddle_height):
            p1_y += -3
        elif p1_y <= paddle_height:
            p1_y += 3
        else:
            p1_y += 3

    # --- Player 2 controls
    if move_up_p2:
        if p2_y >= height:
            p2_y += -3
        elif p2_y <= 0:
            p2_y += 3
        else:
            p2_y += -3


    if move_down_p2:
        if p2_y >= height:
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