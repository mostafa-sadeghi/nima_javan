from random import choice, randint
import pygame
from pygame.sprite import Sprite
from config import WINDOW_HEIGHT, WINDOW_WIDTH


class Monster(Sprite):
    def __init__(self, x, y, image, monster_type):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect = (x, y)

        self.type = monster_type

        self.dx = choice([-1, 1])
        self.dy = choice([-1, 1])

        self.velocity = randint(1, 5)

    def update(self):
        self.rect.x += self.x * self.velocity
        self.rect.y += self.y * self.velocity
