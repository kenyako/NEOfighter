import pygame
from load_image_func import load_image
from global_vars import *
from bullet import Bullet
import json
import os


class Gun(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, Player) -> None:
        pygame.sprite.Sprite.__init__(gun_group)

        # Количество патронов
        if "settings.json" not in os.listdir("./Data"):
            self.cartridges_counter = 10
        else:
            with open(SETTINGS_JSON) as f:
                settings = json.load(f)

            self.cartridges_counter = settings['saves']['count_ammo']

        # Игрок, имеющий это оружие
        self.player = Player

        # Направление стрельбы
        self.rotate_side = "right"

        self.image = load_image('./Sprites/gun.png')
        self.rect = self.image.get_rect().move(
            pos_x * PLATFORM_WIDTH, pos_y * PLATFORM_HEIGHT)

    def shoot(self):
        # Если у игрока имеется оружие и хватает патронов..
        if self.cartridges_counter > 0 and self.player.get_weapon:
            bullet = Bullet(self.rect.x, self.rect.y, self.player)
            all_sprites.add(bullet)
            bullets.add(bullet)

            self.cartridges_counter -= 1

    def update(self, screen):
        if self.player.get_weapon:
            # Привязка оружия к координатам игрока
            self.rect.y = self.player.rect.y + 40
            all_sprites.update()

            if self.player.right:

                if self.rotate_side != "right":
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rotate_side = "right"
                self.rect.x = self.player.rect.x + 7

            else:

                if self.rotate_side != "left":
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rotate_side = "left"
                self.rect.x = self.player.rect.x - 7
        else:
            # Подбор оружия
            if self.rect.x - 20 <= self.player.rect.x <= self.rect.x + 20 and\
                    self.rect.y - 70 <= self.player.rect.y <= self.rect.y + 70:
                self.player.get_weapon = True

        screen.blit(self.image, self.rect)
