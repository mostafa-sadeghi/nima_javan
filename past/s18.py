import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10])
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17+y], [5+x, 7+y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5+x, 7+y], [9+x, 17+y], 2)
    pygame.draw.line(screen, RED, [5+x, 7+y], [1+x, 17+y], 2)

    # Legs
    pygame.draw.line(screen, RED, [5+x, 17+y], [10+x, 27+y], 2)
    pygame.draw.line(screen, RED, [5+x, 17+y], [x, 27+y], 2)


pygame.init()
screen = pygame.display.set_mode((700, 500))

screen.fill(WHITE)

done = True
while done:  # main loop
    for event in pygame.event.get():  # event loop
        if event.type == pygame.QUIT:
            done = False

    screen.fill(WHITE)
    mouse_position = pygame.mouse.get_pos()
    mousex = mouse_position[0]
    mousey = mouse_position[1]
    draw_stick_figure(screen, mousex, mousey)
    pygame.display.flip()
    clock.tick(1)

pygame.quit()
