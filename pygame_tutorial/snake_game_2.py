import pygame
import random

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

snake_icon = pygame.image.load("snake_icon.png")

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Snake~~")
pygame.display.set_icon(snake_icon)


FPS = 20
clock = pygame.time.Clock()

SNAKE_SIZE = 20

head_x = WINDOW_WIDTH/2
head_y = WINDOW_HEIGHT/2 + 100

snake_dx = 0
snake_dy = 0

score = 0

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font("AttackGraffiti.ttf", 32)

title_text = font.render("Snake Game", True, GREEN, DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

score_text = font.render(f"Score: {score}", True, GREEN, DARKRED)
score_rect = title_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAMEOVER", True, RED, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

continue_text = font.render(
    "Press any Key to continue...", True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 50)

apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)


head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)


body_coords = []

runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0

            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1 * SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        # TODO

    display_surface.fill(WHITE)
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
