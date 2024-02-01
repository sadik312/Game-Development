import pygame, time

pygame.init()
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

# Set up the display 
SC_WIDTH = 800
SC_LENGTH = 800
FPS = 60

screen = pygame.display.set_mode((SC_LENGTH, SC_WIDTH))
pygame.display.set_caption("Simple 2D Platformer")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # draw screen
    screen.fill((0,0,0))

    # draw player
    pygame.display.flip()
    
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.move_left()
if keys[pygame.K_RIGHT]:
    player.move_right()
if keys[pygame.K_SPACE]:
    player.jump()

    