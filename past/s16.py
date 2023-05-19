import pygame

pygame.init()
GREEN = (0, 255, 0)
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

pox_x = 0
pox_y = 0
pox_x_change = 1
pox_y_change = 1

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pygame.draw.ellipse(screen, GREEN, [pox_x, pox_y, 10, 10])
    pox_x += pox_x_change
    pox_y += pox_y_change
    if pox_y > 490 or pox_y < 0:
        pox_y_change = -1 * pox_y_change

    if pox_x > 690 or pox_x < 0:
        pox_x_change = -1 * pox_x_change

    pygame.display.flip()
    clock.tick(200)
