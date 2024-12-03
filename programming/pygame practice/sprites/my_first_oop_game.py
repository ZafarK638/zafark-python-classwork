import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        #move the bullet
        self.rect.y += -10

class Block(pygame.sprite.Sprite):
    def __init__(self,colour,width,height) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()

        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0

        self.change_x = 0
        self.change_y = 0
    #end method

    def reset_pos(self):
        # Reset position to the top of the screen, at a random x location
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, width)
    
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1
 
        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1
    #end method

class Player(Block):

    def update(self):
        # Get the current mouse position. 
        pos = width/2,height,2
 
        # Fetch the x and y out of the list,
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = height-50


# Set the width and height of the screen [width, height]
width = 1000
height = 700
size = (width,height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("OOP practise")

pos = width/2
playerSpeed = 10
move_right = False
move_left = False

# Loop until the user clicks the close button.
gameOver = False

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()

for i in range(50):
    # This represents a block
    block = Block(GREEN, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(width)
    block.rect.y = random.randrange(0,height-100)

    block.change_x = random.randrange(-3, 4)
    block.change_y = random.randrange(-3, 4)
    block.left_boundary = 0
    block.top_boundary = 0
    block.right_boundary = width
    block.bottom_boundary = height-100
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
    	
# Create a RED player block
player = Player(RED, 20, 15)
all_sprites_list.add(player)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not gameOver:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #fire a bullet when button pressed
                bullet = Bullet(BLACK,5,5)
                #set bullet location
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False

    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # Call the update() method for all blocks in the block_list
    block_list.update()
    for bullet in bullet_list:
        bullet.update()

    # --- Game logic should go here

    if move_right:
        pos += playerSpeed

    if move_left:
        pos -= playerSpeed

    # --- Screen-clearing code goes here

    screen.fill(WHITE)

    # --- Drawing code should go here
    
    # Fetch the x and y out of the list,
    # Set the player object to the mouse location
    player.rect.x = pos
    player.rect.y = height-50

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    for block in blocks_hit_list:
        score +=1
        print(score)

    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.                    
pygame.quit()