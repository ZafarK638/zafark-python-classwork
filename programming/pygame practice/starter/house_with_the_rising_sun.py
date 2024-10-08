import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)

# Extra colours
sky_blue = (135, 206, 235)
night_sky = (0, 0, 0)
col_sun = (255, 255, 0)
col_moon = (192, 192, 192)


pygame.init()

# Set the width and height of the screen [width, height]
width = 700
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("The House with the Rising Sun")

# Loop until the user clicks the close button.
gameOver = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
fps_limit = 60

# Circle properties
radius = 20  # Radius of the sun
x_pos = 0  # Start at the left of the screen
y_pos = height // 2  # Start at the vertical center of the screen

x_speed = 2  # Move to the right
max_height = 100  # The highest point of the arc

# Initialize the current phase of the sky
is_daytime = True  # Start with daytime

# -------- Main Program Loop ----------- 
while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # --- Game logic for smooth rising and setting sun (arc motion)
    
    x_pos += x_speed  # Move right
    
    # Calculate the distance from the center of the screen (horizontally)
    distance_from_center = abs(x_pos - width // 2)

    # Create a smooth arc using a parabolic-like effect
    # The farther x_pos is from the center, the lower the y_pos
    y_pos = height // 2 - ((1 - (distance_from_center / (width // 2)) ** 2) * max_height)

    # --- Change colors based on position
    if x_pos - radius >= width:  # Check if it reaches the right edge of the screen
        # Reset to the left starting position for the next loop
        x_pos = 0
        
        # Change the phase of the sky after a complete rotation
        is_daytime = not is_daytime  # Toggle between day and night

    # Set background color and sun color based on the phase
    if is_daytime:  # Daytime
        background_color = sky_blue
        sun_color = col_sun
    else:  # Nighttime
        background_color = night_sky
        sun_color = col_moon

    # --- Screen-clearing code
    screen.fill(background_color)

    # --- Drawing code
    pygame.draw.circle(screen, sun_color, [int(x_pos), int(y_pos)], radius)

    ground_height = 50
    pygame.draw.rect(screen, GREEN, [0, height - ground_height, width, ground_height])

    house_size = 50  
    house_x = (width - house_size) // 2  
    house_y = (height - ground_height + (ground_height - house_size) // 2) - ground_height
    pygame.draw.rect(screen, BROWN, [house_x, house_y, house_size, house_size])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(fps_limit)

# Close the window and quit.
pygame.quit()
