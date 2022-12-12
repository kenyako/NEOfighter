import pygame


def draw(screen):
    screen.fill((0, 0, 0))


if __name__ == '__main__':
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("NEOfight")

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
