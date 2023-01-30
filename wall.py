import pygame
from global_vars import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(wall_group)

        self.pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))

        self.pf.fill(pygame.Color(PLATFORM_COLOR))

        self.rect = self.pf.get_rect().move(
            pos_x * PLATFORM_WIDTH, pos_y * PLATFORM_HEIGHT)

    def update(self, screen):
        screen.blit(self.pf, self.rect)
