import pygame
from enemy import Enemy
from constants import *
class Game:
    def __init__(self, player, enemy_group, player_bullet_group,enemy_bullet_group):
        self.score = 0
        self.level_number = 0
        self.player = player
        self.enemy_group = enemy_group
        self.player_bullet_group = player_bullet_group
        self.enemy_bullet_group = enemy_bullet_group
        self.new_level_sound = pygame.mixer.Sound("assets/new_round.wav")

    def if_on_edge(self):
        on_edge = False
        for enemy in self.enemy_group:
            if enemy.rect.right > SCREEN_WIDTH or enemy.rect.left < 0:
                on_edge = True
                break
        if on_edge:
            for enemy in self.enemy_group:
                enemy.direction *= -1
                enemy.rect.y += self.level_number * 50


    def start_new_level(self):
        self.level_number += 1
        for row in range(4):
            for col in range(10):
                enemy = Enemy(col * 64, row * 64 + 100, self.enemy_bullet_group)
                self.enemy_group.add(enemy)


