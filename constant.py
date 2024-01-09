import pygame


class Constant:
    BLACK = pygame.Color("black")
    WHITE = pygame.Color("white")

    SIZE = WIDTH, HEIGHT = (600, 500)
    FPS = 60
    BLOCK = 20
    FIELD_WIDTH, FIELD_HEIGHT = 10, 20
    MARGIN_LEFT = (WIDTH - FIELD_WIDTH * BLOCK) / 2
    MARGIN_TOP = HEIGHT - (FIELD_HEIGHT * BLOCK) - 20
