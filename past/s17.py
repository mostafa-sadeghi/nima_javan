# import pygame
# import random
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# pygame.init()
# screen = pygame.display.set_mode()
# pygame.display.set_caption("My game")
# done = True
# clock = pygame.time.Clock()
# snow_list = []
# for i in range(50):
#     x = random.randrange(0, 1900)
#     y = random.randrange(0, 800)
#     snow_list.append([x, y])
# while done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 done = False
#     screen.fill(BLACK)
#     for i in range(len(snow_list)):
#         pygame.draw.circle(screen, WHITE, snow_list[i],2)
#         snow_list[i][1] += 1
#         if snow_list[i][1] > 800:
#             y = random.randrange(-50,-10)
#             snow_list[i][1] = y
#             x = random.randrange(0,1900)
#             snow_list[i][0] = x
#     pygame.display.flip()
#     clock.tick(60)
# pygame.quit()


# import pygame
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BROWN = (179, 99, 7)
# pygame.init()
# screen = pygame.display.set_mode((700, 500))
# pygame.draw.rect(screen, BROWN, [60, 400, 30, 45])
# pygame.draw.polygon(screen, RED, [[0, 0], [100, 100], [100, 0]])
# pygame.draw.polygon(
#     screen, RED, [(25, 75), (106, 75), (106, 150), (25, 150)], 7)

# done = True
# while done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 done = False
#     pygame.display.flip()

# pygame.quit()


# exercise 1
# یک تابع بساز که کارش کشیدن درخت است
# def fraw_tree()


# def my_func(num1, num2, num3):
# """Return average of three numbers
# num1:int,
# num2:int,
# num3:int
# Returns:float
# """
#     return (num1 + num2 + num3) / 3


# my_func()


# x = 0


# def my_func():
#     global x
#     x += 1


# my_func()
# my_func()
# my_func()
# print(x)


import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (179, 99, 7)
pygame.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

x_coord = 10
y_coord = 10
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("Error, I did not find any joystick.")
else:
    print("ok")
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

# center  (0,0)
# Up Left  (-1,-1)
# Up   (0,-1)
# Up Right  (1,-1)
# Right  (1,0)
# Down Right  (1,1)
# Down   (0,1)
# Down  Left (-1,1)
# Left (-1,0)

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = False

    # pos = pygame.mouse.get_pos()
    # x = pos[0]
    # y = pos[1]

    if joystick_count != 0:
        h_axis_pos = my_joystick.get_axis(0)
        v_axis_pos = my_joystick.get_axis(1)

        x_coord += int(h_axis_pos * 10)
        y_coord += int(v_axis_pos * 10)
    screen.fill(WHITE)
    pygame.draw.rect(screen, BROWN, [x_coord, x_coord, 30, 45])
    pygame.display.flip()
    clock.tick(10)

pygame.quit()


# با کمک تابع آدمک را بکش و همراه ماوس حرکت بده
