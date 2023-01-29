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

with_gun_sprites = [
    image.load('./Data/Sprites/Player/with_gun_1.png'),
    image.load('./Data/Sprites/Player/with_gun_1.png'),
    image.load('./Data/Sprites/Player/with_gun_1.png'),

    image.load('./Data/Sprites/Player/with_gun_2.png'),
    image.load('./Data/Sprites/Player/with_gun_2.png'),
    image.load('./Data/Sprites/Player/with_gun_2.png'),

    image.load('./Data/Sprites/Player/with_gun_3.png'),
    image.load('./Data/Sprites/Player/with_gun_3.png'),
    image.load('./Data/Sprites/Player/with_gun_3.png'),

    image.load('./Data/Sprites/Player/with_gun_2.png'),
    image.load('./Data/Sprites/Player/with_gun_2.png'),
    image.load('./Data/Sprites/Player/with_gun_2.png')
]

mon1_sprite = [
    image.load('./Data/Sprites/monster_f3.png'),
    image.load('./Data/Sprites/monster_f4.png')
]

mon2_sprite = [
    image.load('./Data/Sprites/monster_f1.png'),
    image.load('./Data/Sprites/monster_f2.png')
]

player_anim = 0
monsters_anim = 0

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
    },
    "saves": {
        "coord_x": None,
        "coord_y": None,
        "have_gun": False,
        "count_ammo": 15,
        "count_health": 100,
        "is_continue": False
    }
}

# Файл JSON для сохранения
SETTINGS_JSON = './Data/settings.json'


player_group = sprite.Group()
wall_group = sprite.Group()
portal_group = sprite.Group()
gun_group = sprite.Group()
trampoline_group = sprite.Group()
bullets = sprite.Group()
monster_group = sprite.Group()
