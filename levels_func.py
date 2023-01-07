from wall import Wall
from player import Player


def load_level(filename):
    filename = "Data/" + filename

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None

    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '-':
                Wall(x, y)
            elif level[y][x] == '@':
                new_player = Player(x, y)

    return new_player
