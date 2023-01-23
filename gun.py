import pygame
from LoadImage import load_image
from global_vars import *
from bullet import Bullet


class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y, Player) -> None:
        super().__init__(gun_group)

        self.x, self.y = x, y
        self.cartridges_counter = 10
        self.player = Player

        self.rotate_side = "right"

        self.image = load_image('./Sprites/gun.png')
        self.rect = self.image.get_rect().move(
            self.x * PLATFORM_WIDTH, self.y * PLATFORM_HEIGHT)

    def shoot(self):
        if self.cartridges_counter > 0 and self.player.get_weapon:
            bullet = Bullet(self.rect.x, self.rect.y, self.player)
            all_sprites.add(bullet)
            bullets.add(bullet)

            self.cartridges_counter -= 1

    def update(self, screen):
        if self.player.get_weapon:
            self.rect.y = self.player.rect.y + 40
            all_sprites.update()

            if not self.player.right:
                if self.rotate_side != "left":
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rotate_side = "left"
                self.rect.x = self.player.rect.x - 7

            if self.player.right:
                if self.rotate_side != "right":
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rotate_side = "right"
                self.rect.x = self.player.rect.x + 7
        else:
            if self.rect.x - 20 <= self.player.rect.x <= self.rect.x + 20 and\
                    self.rect.y - 70 <= self.player.rect.y <= self.rect.y + 70:
                self.player.get_weapon = True

        screen.blit(self.image, self.rect)
