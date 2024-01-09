import pygame

from constant import Constant


class Field:

    def __init__(self):
        self.matrix = [[0] * Constant.FIELD_WIDTH for i in range(Constant.FIELD_HEIGHT)]

    def draw_field(self, screen):
        for y in range(Constant.FIELD_HEIGHT):
            for x in range(Constant.FIELD_WIDTH):
                pygame.draw.rect(screen, Constant.WHITE, (Constant.MARGIN_LEFT + x * Constant.BLOCK,
                                                          Constant.MARGIN_TOP + y * Constant.BLOCK,
                                                          Constant.BLOCK, Constant.BLOCK), 1)

    def add_block(self):
        pass
