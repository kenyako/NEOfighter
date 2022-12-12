import pygame


class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width  # Длина кнопки
        self.height = height  # Ширина кнопки
        self.inactive_color = inactive_color  # Базовый цвет
        self.active_color = active_color  # Цвет при наведении

    def draw(self, btn_x, btn_y, btn_text=None, action=None):
        mouse = pygame.mouse.get_pos()  # Позиция мыши
        click = pygame.mouse.get_pressed()  # Обработка нажатия на кнопку мыши

        # Если курсор в пределах кнопки..
        if btn_x < mouse[0] < btn_x + self.width and \
                btn_y < mouse[1] < btn_y + self.height:

            # Отрисовываем кнопку с цветом <active_color>
            pygame.draw.rect(
                screen,
                self.active_color,
                (btn_x, btn_y, self.width, self.height)
            )

            # Если по ней кликнули ЛКМ и ключ action задан
            if click[0] == 1 and action is not None:
                action()  # Запускаем функцию, переданную по ключу action

        # А ели за пределами кнопки..
        else:
            # Отрисовываем кнопку со стандартным цветом
            pygame.draw.rect(
                screen,
                self.inactive_color,
                (btn_x, btn_y, self.width, self.height)
            )

        # Отрисовываем текст на кнопке
        text_on_btn = pygame.font.Font("./Fonts/retro-land-mayhem.ttf", 20)\
            .render(btn_text, True, COLORS['second_text'])
        screen.blit(
            text_on_btn,
            (btn_x + (self.width // 2 - text_on_btn.get_width() // 2),
                btn_y + (self.height // 2 - text_on_btn.get_height() // 2))
                )


def end_screen(screen, text_on_screen):
    """
    Конечный экран игры, на котором отображается надпись <text_on_screen>
    и кнопка перезапуска
    """

    # Закрашиваем окно
    screen.fill(COLORS['main'])

    # Отрисовываем текст с результатом
    font_size = 60
    font = pygame.font.Font('./Fonts/retro-land-mayhem.ttf', font_size)
    text = font.render(text_on_screen, True, COLORS['text'])

    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 75

    screen.blit(text, (text_x, text_y))

    btn_width, btn_height = 300, 100

    # Создаем экземпляр класса Button (кнопку на экране завершения игры)
    btn = Button(
        btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

    # Отрисовываем кнопку на нужных координатах
    btn.draw(
        width // 2 - btn_width // 2,
        height // 2 - btn_height // 2 + 50,
        "Restart", start_screen(screen))


def start_screen(screen):
    """
    Стартовый экран игры
    """
    pass


# Словарь с цветами, используемыми в коде
COLORS = {
    'main': '#222831',
    'second_main': '#393E46',
    'text': '#FFD369',
    'second_text': '#EEEEEE',
    'btn_inactive_color': "#393E46",
    'btn_active_color': "#4f5257"
}

# Запускаем сие чудо
if __name__ == '__main__':
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("NEOfight")

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        end_screen(screen, "You Win!")
        pygame.display.flip()

    pygame.quit()
