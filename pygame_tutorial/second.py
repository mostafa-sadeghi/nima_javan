import pygame
import sys
import os
pygame.init()

if getattr(sys, 'frozen', False):
    wd = sys._MEIPASS
else:
    wd = ''
# family_image = pygame.image.load(
#     os.path.join(wd, 'folder', "family.jpg")).convert()
# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
BLACK = (0, 0, 0)


sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_2 = pygame.mixer.Sound('sound_2.wav')

# sound_1.play()
# pygame.time.delay(2000)
# sound_2.play()
# pygame.time.delay(2000)
# sound_2.set_volume(0.2)
# sound_2.play()

pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1, 0.0)
# pygame.time.delay(5000)
# pygame.mixer.music.stop()

system_font = pygame.font.SysFont('calibri', 64)
system_text = system_font.render("Dragon game",
                                 True, GREEN, DARK_GREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2,
                           WINDOW_HEIGHT//2)

custom_font = pygame.font.Font("AttackGraffiti.ttf", 32)

custom_text = custom_font.render("Dragon", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)


display_surface = pygame.display.set_mode((WINDOW_WIDTH,
                                           WINDOW_HEIGHT))
pygame.display.set_caption("Second Game")
dragon_left_image = pygame.image.load(os.path.join(wd,
                                                   '',
                                      "dragon_left.png"))
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load(
    os.path.join(wd, '', "dragon_right.png"))
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH // 2
dragon_rect.bottom = WINDOW_HEIGHT


VELOCITY = 30

# The main game loop
running = True
while running:
    # Loop through a list of event objects that have occured
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
    display_surface.fill((0, 0, 0))
    # Blit (copy) a surface object at the given coordinates to our display
    display_surface.blit(dragon_left_image,
                         dragon_left_rect)
    display_surface.blit(dragon_right_image,
                         dragon_right_rect)
    # display_surface.blit(system_text,
    #                      system_text_rect)

    # display_surface.blit(custom_text, custom_text_rect)

    pygame.draw.line(display_surface,
                     (255, 255, 255),
                     (0, 75), (WINDOW_WIDTH, 75))

    display_surface.blit(dragon_image, dragon_rect)

    # Update the display
    pygame.display.update()
pygame.quit()
