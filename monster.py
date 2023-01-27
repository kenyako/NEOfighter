import pygame
from load_image_func import load_image
from global_vars import *


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__(monster_group)

        self.x, self.y = x, y

        self.image = load_image('./Sprites/monster_f1.png')

        self.rect = self.image.get_rect().move(
            self.x * PLATFORM_WIDTH, self.y * PLATFORM_HEIGHT)

        self.monster_health = 100

    def update(self, screen):
        global monsters_anim

        self.image = mon2_sprite[monsters_anim]

        if monsters_anim == 1:
            monsters_anim = 0

        else:
            monsters_anim += 1

        screen.blit(self.image, self.rect)
