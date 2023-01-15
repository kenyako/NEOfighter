from pygame import image, sprite

'''
В данном файле содержатся глобальные переменные
Для оптимального доступа из любого файла
'''

# Ссылка на репозиторий
gh_link = 'https://github.com/kenyako/NEOfighter'

# Размеры окна
size = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Характеристики персонажа
character_speed = 10

# Спрайты ходьбы
go_sprites = [
    image.load('./Data/Sprites/Player/goes_right.png'),
    image.load('./Data/Sprites/Player/goes_right.png'),
    image.load('./Data/Sprites/Player/goes_right.png'),

    image.load('./Data/Sprites/Player/stand_right.png'),
    image.load('./Data/Sprites/Player/stand_right.png'),
    image.load('./Data/Sprites/Player/stand_right.png'),

    image.load('./Data/Sprites/Player/goes_right2.png'),
    image.load('./Data/Sprites/Player/goes_right2.png'),
    image.load('./Data/Sprites/Player/goes_right2.png'),

    image.load('./Data/Sprites/Player/stand_right.png'),
    image.load('./Data/Sprites/Player/stand_right.png'),
    image.load('./Data/Sprites/Player/stand_right.png')
]

player_anim = 0

# Словарь с цветами, используемыми в коде
COLORS = {
    'main': '#222831',
    'second_main': '#393E46',
    'text': '#FFD369',
    'second_text': '#EEEEEE',
    'btn_inactive_color': "#393E46",
    'btn_active_color': "#4f5257",
    "btn_disable_color": "#2e3136",
    "platform_color": "#222831",
    "empty_color": '#393E46'
}

# Характеристики уровня
PLATFORM_COLOR = COLORS["platform_color"]
EMPTY_COLOR = COLORS["empty_color"]
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32

# Шрифт
FONT = './Data/Fonts/retro-land-mayhem.ttf'

# Переменная для считывании состоянии кнопки
alreadyPressed = False


settings_temp = {
    "scenes": {
        "currency_screen": "start",
        "last_scene": "start"
    }
}

# Файл JSON для сохранения
SETTINGS_JSON = './Data/settings.json'


player_group = sprite.Group()
wall_group = sprite.Group()
gun_group = sprite.Group()
trampoline_group = sprite.Group()
