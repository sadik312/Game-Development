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
        if event.type == pygame.KEYDOWN:
            if pygame.key == pygame.K_LALT:
                print(1)
                screen.fill(RED)
            if pygame.key == pygame.K_3:
                screen.fill(BLUE)
            if pygame.key == pygame.K_2:
                screen.fill(GREEN)
                pygame.display.update()
    
    