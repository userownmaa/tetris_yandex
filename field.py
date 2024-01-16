import pygame

from constant import Constant


class Field:

    def __init__(self):
        self.matrix = [[0] * Constant.FIELD_WIDTH for i in range(Constant.FIELD_HEIGHT)]

    def draw_field(self, screen):
        for y in range(Constant.FIELD_HEIGHT):
            for x in range(Constant.FIELD_WIDTH):
                pygame.draw.rect(screen, Constant.WHITE, (Constant.MARGIN_LEFT * Constant.BLOCK + x * Constant.BLOCK,
                                                          Constant.MARGIN_TOP * Constant.BLOCK + y * Constant.BLOCK,
                                                          Constant.BLOCK, Constant.BLOCK), 1)

    def add_block(self, bottom_group):
        for sprite in bottom_group:
            x, y = sprite.get_position()
            self.matrix[y - 2][x - 2] = 1
        print(self.matrix)

    def remove_row(self, row):
        for x in range(len(row)):
            self.matrix[row][x] = 0
        print(self.matrix)

    def is_row_completed(self, bottom_group):
        completed = list()
        for i in range(len(self.matrix)):
            if all(self.matrix[i]):
                completed.append(i)
        for row in completed:
            self.remove_row(row)



