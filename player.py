import pygame
import json
from global_vars import *
from load_image_func import *


class Player(pygame.sprite.Sprite):
    right = True
    is_jump = False

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group)

        # Загружаем изображение с начальной позицией игрока
        self.image = load_image('./Sprites/Player/stand_sraight.png')
        self.rect = self.image.get_rect().move(
            pos_x * PLATFORM_WIDTH, pos_y * PLATFORM_HEIGHT)

        self.change_x = 0
        self.change_y = 0

        # Имеется ли у игрока оружие
        if "settings.json" not in os.listdir("./Data"):
            self.get_weapon = False
        else:
            with open(SETTINGS_JSON) as f:
                settings = json.load(f)

            self.get_weapon = settings['saves']['have_gun']

    def update(self, screen):
        global player_anim

        self.calc_grav()

        with open(SETTINGS_JSON) as f:
            settings = json.load(f)

        if settings['saves']['coord_x']:

            cur_x = settings['saves']['coord_x']
            cur_y = settings['saves']['coord_y']

            self.rect.x = cur_x
            self.rect.y = cur_y

            settings['saves']['coord_x'] = None
            settings['saves']['coord_y'] = None

            with open(SETTINGS_JSON, "w") as f:
                f.write(json.dumps(settings))

        self.rect.x += self.change_x

        # Отслеживание столкновений с поверхностями по горизонтали
        block_hit_list = pygame.sprite.spritecollide(self, wall_group, False)

        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        # Отслеживание столкновений с поверхностями по вертикали
        block_hit_list = pygame.sprite.spritecollide(self, wall_group, False)

        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

        if self.change_y == 0:
            self.is_jump = False
            self.image = load_image('./Sprites/Player/stand_sraight.png')

        # Отслеживание столкновений с батутом по вертикали
        block_hit_list = pygame.sprite.spritecollide(
            self, trampoline_group, False)

        for block in block_hit_list:
            self.jump(20)
            break

        if self.change_y == 0:
            self.is_jump = False
            self.image = load_image('./Sprites/Player/stand_sraight.png')

        block_hit_list = pygame.sprite.spritecollide(self, portal_group, False)

        for block in block_hit_list:
            pass

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

    def jump(self, jump_forge=10):
        self.is_jump = True

        # Проверка на то, в какую сторону смотрит игрок в момент прыжка
        if self.right:
            self.image = load_image('./Sprites/Player/jump_right.png')
        else:
            self.image = pygame.transform.flip(
                load_image('./Sprites/Player/jump_right.png'), True, False)

        self.rect.y += jump_forge
        platform_hit_list = pygame.sprite.spritecollide(
            self, wall_group, False)
        self.rect.y -= jump_forge

        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -jump_forge - 5

    def go_left(self):
        self.change_x = -character_speed

        # Проверка на поворот в прыжке
        if self.right and self.is_jump:
            self.image = pygame.transform.flip(
                load_image('./Sprites/Player/jump_right.png'), True, False)

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
            self.image = load_image('./Sprites/Player/stand_sraight.png')

        self.change_x = 0
