import pygame
from global_vars import *
from LoadImage import *


class Player(pygame.sprite.Sprite):
    right = True
    is_jump = False

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group)

        # Загружаем изображение с начальной позицией игрока
        self.image = load_image('./Sprites/stand_sraight.png')
        self.rect = self.image.get_rect().move(
            pos_x * PLATFORM_WIDTH, pos_y * PLATFORM_HEIGHT)

        self.change_x = 0
        self.change_y = 0

    def update(self, screen):
        global player_anim

        self.calc_grav()

        self.rect.x += self.change_x

        # Отслеживание столкновений с поверхностями по горизонтали
        block_hit_list = pygame.sprite.spritecollide(self, wall_group, False)

        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        # Отслеживание столкновений с поверхностями по вертиками
        block_hit_list = pygame.sprite.spritecollide(self, wall_group, False)

        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

        if self.change_y == 0:
            self.is_jump = False
            self.image = load_image('./Sprites/stand_sraight.png')

        # Если персонаж находится в гориз. движении и не прыгает,
        # то мы пролистываем кадры ходьбы
        if self.change_x != 0 and not self.is_jump:

            self.image = go_sprites[player_anim]

            if player_anim == 3:
                player_anim = 0
            else:
                player_anim += 1

            if not self.right:
                self.image = pygame.transform.flip(self.image, True, False)

        screen.blit(self.image, self.rect)

    def calc_grav(self):
        """Гравитация игрока"""

        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.95

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height\
                and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        self.is_jump = True

        # Проверка на то, в какую сторону смотрит игрок в момент прыжка
        if self.right:
            self.image = load_image('./Sprites/jump_right.png')
        else:
            self.image = pygame.transform.flip(
                load_image('./Sprites/jump_right.png'), True, False)

        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(
            self, wall_group, False)
        self.rect.y -= 10

        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -15

    def go_left(self):
        self.change_x = -character_speed

        # Проверка на поворот в прыжке
        if self.right and self.is_jump:
            self.image = pygame.transform.flip(
                load_image('./Sprites/jump_right.png'), True, False)

        self.right = False

    def go_right(self):
        self.change_x = character_speed

        if not self.right and self.is_jump:
            self.image = pygame.transform.flip(self.image, True, False)

        self.right = True

    def stop(self):
        # Если персонаж находится не в прыжке,
        # он принимает свою обычную позицию
        if not self.is_jump:
            self.image = load_image('./Sprites/stand_sraight.png')

        self.change_x = 0
