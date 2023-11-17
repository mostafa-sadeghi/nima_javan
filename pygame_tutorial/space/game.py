import pygame
from enemy import Enemy

class Game:
    def __init__(self, player, enemy_group, player_bullet_group,enemy_bullet_group):
        self.score = 0
        self.level_number = 0
        self.player = player
        self.enemy_group = enemy_group
        self.player_bullet_group = player_bullet_group
        self.enemy_bullet_group = enemy_bullet_group
        self.new_level_sound = pygame.mixer.Sound("assets/new_round.wav")

    def start_new_level(self):
        self.level_number += 1
        for row in range(4):
            for col in range(10):
                enemy = Enemy(col * 64, row * 64, self.enemy_bullet_group)
                self.enemy_group.add(enemy)


