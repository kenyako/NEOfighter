import pygame
import json

from global_vars import *
from button import Button


class ContinueButton(Button):
    def __init__(
           self, screen, width, height,
           inactive_color=None, active_color=None, isActive=False
         ):
        super().__init__(screen, width, height, inactive_color, active_color)

        self.isActive = isActive

    def draw(self, btn_x, btn_y, btn_text, action=None, btn_image=None):
        global alreadyPressed

        with open('./settings.json') as f:
            settings = json.load(f)

        last_scene = settings['scenes']['last_scene']

        if last_scene not in ["start", "win", "lose"]:
            self.isActive = True
        else:
            self.isActive = False

        # Позиция мыши
        mouse = pygame.mouse.get_pos()
        # Обработка нажатия на кнопку мыши
        click = pygame.mouse.get_pressed()

        # Если курсор в пределах кнопки..
        if btn_x < mouse[0] < btn_x + self.width and \
                btn_y < mouse[1] < btn_y + self.height and self.isActive:

            if btn_text:
                # Отрисовываем кнопку с цветом <active_color>
                pygame.draw.rect(
                    self.screen,
                    self.active_color,
                    (btn_x, btn_y, self.width, self.height)
                )

            # Если по ней кликнули ЛКМ и ключ action задан
            if click[0] and action is not None:
                alreadyPressed = True
            else:
                if alreadyPressed:
                    action()
                    alreadyPressed = False

        # А если за пределами кнопки..
        else:
            # Выбираем цвет кнопки в зависимости от её активности
            if self.isActive:
                color = COLORS["btn_inactive_color"]
            else:
                color = COLORS["btn_disable_color"]

            if btn_text:
                # Отрисовываем кнопку с заданым цветом
                pygame.draw.rect(
                    self.screen, color,
                    (btn_x, btn_y, self.width, self.height)
                )

        if btn_text:
            # Отрисовываем текст на кнопке
            _fontSize = 30
            text_on_btn = pygame.font.Font(
                FONT,
                _fontSize
            )\
                .render(btn_text, True, COLORS['second_text'])
            self.screen.blit(
                text_on_btn,
                (btn_x + (self.width // 2 - text_on_btn.get_width() // 2),
                    btn_y + (
                        self.height // 2 - text_on_btn.get_height() // 2
                        ))
            )

        # Если передан путь к картинке..
        elif btn_image is not None:
            # Отрисовываем картинку на кнопке
            image_on_btn = pygame.image.load(btn_image)
            image_rect = image_on_btn.get_rect(
                topleft=(btn_x, btn_y))
            self.screen.blit(
                image_on_btn,
                image_rect
            )
