import pygame
from load_image_func import *
from global_vars import *


class Portal(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(portal_group)

        # ДОРАБОТАТЬ ПОРТАЛЫ
        self.image = load_image('./Sprites/secondary_portal.png')
        self.rect = self.image.get_rect().move(
            pos_x * PLATFORM_WIDTH, (pos_y * PLATFORM_HEIGHT))
