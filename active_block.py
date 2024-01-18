import copy
import random

import pygame

from constant import Constant
from square import Square


class ActiveBlock:

    def __init__(self, block_type, color, *groups):
        self.block_type = block_type
        self.color = color
        self.rotation = 1
        self.coords = copy.deepcopy(Constant.BLOCKS_START_POSITION[block_type])
        for c in self.coords:
            c[0] += Constant.START_X
            c[1] += Constant.START_Y
        for square in self.coords:
            Square(square[0] * Constant.BLOCK, square[1] * Constant.BLOCK, self.color, *groups)

    def move_side(self, direction, active_block_group):
        if direction == "L":
            for sprite in active_block_group:
                sprite.move_left(Constant.LEFT_X, Constant.LEFT_Y)
            self.update_coords(Constant.LEFT_X, Constant.LEFT_Y)
        elif direction == "R":
            for sprite in active_block_group:
                sprite.move_left(Constant.RIGHT_X, Constant.RIGHT_Y)
            self.update_coords(Constant.RIGHT_X, Constant.RIGHT_Y)

    def move_down(self, active_block_group):
        for sprite in active_block_group:
            sprite.move_down(Constant.DOWN_X, Constant.DOWN_Y)
        self.update_coords(Constant.DOWN_X, Constant.DOWN_Y)

    def move_up(self, active_block_group):
        for sprite in active_block_group:
            sprite.move_up(Constant.UP_X, Constant.UP_Y)
        self.update_coords(Constant.DOWN_X, Constant.DOWN_Y)

    def rotate(self, active_block_group):
        i = 0
        for sprite in active_block_group:
            if self.rotation == 4:
                x = Constant.BLOCKS_POSITION_1[self.block_type][i][0]
                y = Constant.BLOCKS_POSITION_1[self.block_type][i][1]
                sprite.rotate(x * Constant.BLOCK, y * Constant.BLOCK)
                i += 1
            if self.rotation == 1:
                x = Constant.BLOCKS_POSITION_2[self.block_type][i][0]
                y = Constant.BLOCKS_POSITION_2[self.block_type][i][1]
                sprite.rotate(x * Constant.BLOCK, y * Constant.BLOCK)
                i += 1
            if self.rotation == 2:
                x = Constant.BLOCKS_POSITION_3[self.block_type][i][0]
                y = Constant.BLOCKS_POSITION_3[self.block_type][i][1]
                sprite.rotate(x * Constant.BLOCK, y * Constant.BLOCK)
                i += 1
            if self.rotation == 3:
                x = Constant.BLOCKS_POSITION_4[self.block_type][i][0]
                y = Constant.BLOCKS_POSITION_4[self.block_type][i][1]
                sprite.rotate(x * Constant.BLOCK, y * Constant.BLOCK)
                i += 1
        self.rotation += 1
        if self.rotation > 4:
            self.rotation = 1

    def stop(self, active_block_group, bottom_group):
        for sprite in active_block_group:
            active_block_group.remove(sprite)
            bottom_group.add(sprite)

    def is_at_bottom(self, active_block_group, bottom_group):
        for sprite in active_block_group:
            if pygame.sprite.spritecollideany(sprite, bottom_group):
                return True
            if sprite.get_position()[1] == Constant.BOTTOM_BORDER:
                return True
        return False

    def is_out_of_border(self, active_block_group):
        for sprite in active_block_group:
            if sprite.get_position()[0] == Constant.RIGHT_BORDER:
                return "R"
            elif sprite.get_position()[0] == Constant.LEFT_BORDER:
                return "L"
        return None

    def update_coords(self, x, y):
        for pos in self.coords:
            pos[0] += x // Constant.BLOCK
            pos[1] += y // Constant.BLOCK



