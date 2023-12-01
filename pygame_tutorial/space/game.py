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
        # second way
        self.enemy_hit_sound = pygame.mixer.Sound("assets/alien_hit.wav")
        
        self.font72 = pygame.font.Font("assets/Facon.ttf", 72)
        self.font32 = pygame.font.Font("assets/Facon.ttf", 32)

    def check_enemy_hit(self):
        # first way
        # temp = pygame.sprite.groupcollide(self.player_bullet_group, self.enemy_group, True, True)
        # if temp:
        #     self.score += 1
        #     for item in temp.values():
        #         item[0].enemy_hit_sound.play()

        # second way
        if pygame.sprite.groupcollide(self.player_bullet_group, self.enemy_group, True, True):
            self.enemy_hit_sound.play()
            self.score += 1


    def if_on_edge(self):
        on_edge = False
        for enemy in self.enemy_group:
            if enemy.rect.right > SCREEN_WIDTH or enemy.rect.left < 0:
                on_edge = True
                break
        if on_edge:
            if_on_safe_zone = False
            for enemy in self.enemy_group:
                enemy.direction *= -1
                enemy.rect.y += self.level_number * 300
                if enemy.rect.bottom >= SCREEN_HEIGHT - self.player.image.get_height():
                    if_on_safe_zone = True
            if if_on_safe_zone:
                
                self.reset_game()

    def draw(self):
        """
        نمایش دادن 
        امتیاز
        شماره مرحله
        جان بازیکن
        در بالای صفحه
        """
        pass

    def reset_game(self):
        last_reset_time = pygame.time.get_ticks()
        self.score = 0
        self.level_number = 0
        self.player.lives = 3
        self.enemy_group.empty() 
        self.player_bullet_group.empty() 
        self.enemy_bullet_group.empty()
        reset_text = self.font72.render("You Lose", True, (240, 15,230))
        reset_rect = reset_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        while pygame.time.get_ticks() - last_reset_time < 5000:
            screen.fill((0,0,0))
            screen.blit(reset_text,reset_rect)
            pygame.display.update()
        self.start_new_level()
        
    
    
    def start_new_level(self):
        self.level_number += 1
        for row in range(4):
            for col in range(10):
                enemy = Enemy(col * 64, row * 64 + 100, self.enemy_bullet_group)
                self.enemy_group.add(enemy)


