import pygame.sprite

from constant import Constant
from image import Image
import random


class Square(pygame.sprite.Sprite):

    img = Image()
    color_blocks = {
        1: img.load_image("red.jpg"),
        2: img.load_image("orange.jpg"),
        3: img.load_image("yellow.jpg"),
        4: img.load_image("green.jpg"),
        5: img.load_image("blue.jpg"),
        6: img.load_image("purple.jpg")
    }

    def __init__(self, block_type, x, y, color, *groups):
        super().__init__(*groups)
        self.image = self.color_blocks[color]
        self.rect = self.image.get_rect().move(x, y)

    def turn(self, matrix, coords):
        pass
    # повернуть матрицу
