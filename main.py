import pygame


class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    def draw(self, btn_x, btn_y, btn_text=None, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if btn_x < mouse[0] < btn_x + self.width and \
                btn_y < mouse[1] < btn_y + self.height:
            pygame.draw.rect(
                screen,
                self.active_color,
                (btn_x, btn_y, self.width, self.height)
            )

            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(
                screen,
                self.inactive_color,
                (btn_x, btn_y, self.width, self.height)
            )

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
    btn = Button(
        btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

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
