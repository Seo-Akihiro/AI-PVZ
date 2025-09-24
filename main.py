import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plants vs. Zombies")

# Load images
class Plant:
    def __init__(self, x, y):
        self.image = pygame.image.load('plant.png')
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Zombie:
    def __init__(self, x, y):
        self.image = pygame.image.load('zombie.png')
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def move(self):
        self.rect.x -= 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Game loop
plants = [Plant(100, 500)]
zombies = [Zombie(800, 500)]
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    # Update zombies
    for zombie in zombies:
        zombie.move()
        zombie.draw(screen)

    # Draw plants
    for plant in plants:
        plant.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()