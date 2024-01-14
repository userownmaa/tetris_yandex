import copy
import random

import pygame

from constant import Constant
from square import Square


class ActiveBlock:

    def __init__(self, block_type, color, *groups):
        matrix = copy.deepcopy(Constant.BLOCKS_MATRIX[block_type])
        self.color = color
        self.coords = list()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    self.coords.append([Constant.START_X + j,
                                        Constant.START_Y + i])
                    matrix[i][j] = 2
        for square in self.coords:
            Square(square[0] * Constant.BLOCK, square[1] * Constant.BLOCK, self.color, *groups)

    def move_side(self, direction, active_block_group):
        if direction == "L":
            for sprite in active_block_group:
                sprite.move_left(Constant.LEFT_X, Constant.LEFT_Y)
        elif direction == "R":
            for sprite in active_block_group:
                sprite.move_left(Constant.RIGHT_X, Constant.RIGHT_Y)

    def move_down(self, active_block_group):
        for sprite in active_block_group:
            sprite.move_down(Constant.DOWN_X, Constant.DOWN_Y)
        for pos in self.coords:
            pos[0] += Constant.DOWN_X // Constant.BLOCK
            pos[1] += Constant.DOWN_Y // Constant.BLOCK

    def move_back(self, active_block_group):
        for sprite in active_block_group:
            sprite.move_back(Constant.UP_X, Constant.UP_Y)
        for pos in self.coords:
            pos[0] += Constant.UP_X // Constant.BLOCK
            pos[1] += Constant.UP_Y // Constant.BLOCK

    def stop(self, active_block_group, bottom_group):
        for sprite in active_block_group:
            active_block_group.remove(sprite)
            bottom_group.add(sprite)

    def is_at_bottom(self, active_block_group, bottom_group):
        for pos in self.coords:
            if pos[1] == Constant.BOTTOM_BORDER:
                return True
        for sprite in active_block_group:
            if pygame.sprite.spritecollideany(sprite, bottom_group):
                return True
        return False


