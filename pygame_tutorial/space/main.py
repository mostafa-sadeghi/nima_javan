import pygame
from constants import *
from player import Player
pygame.init()



clock = pygame.time.Clock()
player_bullet_group = pygame.sprite.Group()
my_player = Player(player_bullet_group)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                my_player.fire()
    screen.fill((0,0,0))
    my_player.move()
    my_player.draw(screen)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
