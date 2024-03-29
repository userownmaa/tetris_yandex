import pygame.sprite

from constant import Constant
from image import Image


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

    def __init__(self, x, y, color, *groups):
        super().__init__(*groups)
        self.image = self.color_blocks[color]
        self.rect = self.image.get_rect().move(x, y)
        self.coords = self.x, self.y = x // Constant.BLOCK, y // Constant.BLOCK

    def move_down(self, x, y):
        self.rect = self.rect.move(x, y)
        self.x += x // Constant.BLOCK
        self.y += y // Constant.BLOCK

    def move_up(self, x, y):
        self.rect = self.rect.move(x, y)
        self.x += x // Constant.BLOCK
        self.y += y // Constant.BLOCK

    def move_right(self, x, y):
        self.rect = self.rect.move(x, y)
        self.x += x // Constant.BLOCK
        self.y += y // Constant.BLOCK

    def move_left(self, x, y):
        self.rect = self.rect.move(x, y)
        self.x += x // Constant.BLOCK
        self.y += y // Constant.BLOCK

    def rotate(self, x, y):
        self.rect = self.rect.move(x, y)
        self.x += x // Constant.BLOCK
        self.y += y // Constant.BLOCK

    def get_position(self):
        return self.x, self.y
