import pygame
from LoadImage import load_image
from global_vars import *


class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__(gun_group)

        self.image = load_image('./Sprites/gun.png')
        self.rect = self.image.get_rect().move(
            x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT)
