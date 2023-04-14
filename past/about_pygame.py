# import turtle

# s = turtle.Screen()
# p = turtle.Pen()
# p.home()
# s.exitonclick()

# import pygame

# pygame.init()
# # Define colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# LIGHT_PURPLE = (218, 205, 255)
# size = (700, 500)

# screen = pygame.display.set_mode(size)
# done = False
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         elif event.type == pygame.KEYDOWN:
#             print("User pressed a key...")
#         elif event.type == pygame.KEYUP:
#             print("User released a key...")
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print("User pressed a mouse button ....")

#     screen.fill(WHITE)
    # pygame.draw.rect(screen, LIGHT_PURPLE, [50, 50, 100, 200])
    # pygame.draw.line(screen, BLACK, [0, 0], [100, 100],5)

    # y_offset = 0
    # while y_offset < 100:
    #     pygame.draw.line(
    #         screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 4)
    #     y_offset += 10

    #  تمرین

    # کشیدن 10 ضربدر

    # pygame.draw.ellipse(screen, GREEN,[20,20,250,100])
    # pygame.draw.polygon(screen, BLACK, [[100,100], [0,200], [200,200]])
    # font = pygame.font.SysFont('Arial', 25, True, False)
    # score = 10
    # text = font.render('Score: '+str(score), BLACK, GREEN)
    # screen.blit(text, [0, 0])
    # pygame.display.flip()
