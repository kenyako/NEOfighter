import pygame
from LoadImage import load_image
from global_vars import *


class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__(gun_group)

        self.x, self.y = x, y

        self.image = load_image('./Sprites/gun.png')
        self.rect = self.image.get_rect().move(
            self.x * PLATFORM_WIDTH, self.y * PLATFORM_HEIGHT)
