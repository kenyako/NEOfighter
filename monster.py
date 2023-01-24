import pygame
from load_image_func import load_image
from global_vars import *


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__(monster_group)

        self.x, self.y = x, y

        self.image = load_image('./Sprites/mon_second1.png')
        self.rect = self.image.get_rect().move(
            self.x * PLATFORM_WIDTH, self.y * PLATFORM_HEIGHT)
