import os
import pygame
import sys
from constant import Constant


pygame.init()
screen = pygame.display.set_mode(Constant.SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("TETRIS")


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = []

    fon = pygame.transform.scale(load_image(""), (Constant.WIDTH, Constant.HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, Constant.BLACK)
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(Constant.FPS)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def run_game():




def main():
    # start_screen()
    running = True
    while running:
        clock.tick(Constant.FPS)
        screen.fill(Constant.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    terminate()


if __name__ == '__main__':
    sys.exit(main())