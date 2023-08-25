from random import randint
import pygame
from config import WINDOW_HEIGHT, WINDOW_WIDTH

from monster import Monster


class Game:
    def __init__(self, player, monster_group) -> None:
        self.score = 0
        self.round_number = 0

        self.round_time = 0

        self.next_level_sound = pygame.mixer.Sound("assets/next_level.wav")

        self.player = player
        self.monster_group = monster_group
        self.font = pygame.font.Font("assets/Abrushow.ttf", 24)

        # blue_monster = pygame.image.load

    def update(self):
        pass
        """checking collisions"""

    def draw(self, display_surface):

        # render scoreboard texts

        # display_surface.blit()
        pass

    def start_new_round(self):
        self.round_number += 1
        for i in range(self.round_number):
            self.monster_group.add(
                Monster(
                    randint(0, WINDOW_WIDTH-64),
                    randint(100, WINDOW_HEIGHT-100),

                )
            )
