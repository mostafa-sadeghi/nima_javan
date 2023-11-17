from pygame.sprite import Sprite
import pygame
from constants import *


class Enemy(Sprite):
    def __init__(self,x,y,bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.bullet_group = bullet_group
        self.direction = 1
        self.speed = 2
        
    def update(self):
        self.rect.x += self.direction * self.speed
