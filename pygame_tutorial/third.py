import pygame
from random import choice

from pygame_tutorial.first import YELLOW

pygame.init()


FPS = 60
PLAYER_STARTING_LIVES = 5
CLOWNS_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = 0.5
score = 0


player_lives = PLAYER_STARTING_LIVES
clown_velocity = CLOWNS_STARTING_VELOCITY

clown_dx = choice([-1, 1])
clown_dy = choice([-1, 1])


my_color = (216, 38, 22)
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)


pygame.quit()
