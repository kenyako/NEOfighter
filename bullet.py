from global_vars import *
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, Player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 5))
        self.image.fill("YELLOW")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

        self.player = Player

        if self.player.right:
            self.speedy = 20
        else:
            self.speedy = -20

    def update(self):
        self.rect.x += self.speedy

        # Столкновение со стенами и мобами
        block_hit_list = pygame.sprite.spritecollide(self, wall_group, False)
        hits = pygame.sprite.spritecollide(self, mobs_group, False)

        if hits:
            # Убиваем моба
            self.kill()
        elif block_hit_list:
            self.kill()
