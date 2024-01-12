import random

from constant import Constant
from square import Square


class ActiveBlock:

    blocks = {
        "O": [[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]],
        "T": [[0, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 0, 0]],
        "I": [[0, 0, 0, 0],
              [1, 1, 1, 1],
              [0, 0, 0, 0],
              [0, 0, 0, 0]],
        "L": [[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0]],
        "Z": [[0, 0, 0, 0],
              [1, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]],
        "Z_rev": [[0, 0, 0, 0],
                  [0, 1, 1, 0],
                  [1, 1, 0, 0],
                  [0, 0, 0, 0]],
        "L_rev": [[0, 0, 0, 0],
                  [0, 1, 1, 0],
                  [0, 0, 1, 0],
                  [0, 0, 1, 0]]
    }

    def __init__(self, block_type, *groups):
        self.matrix = self.blocks[block_type]
        self.coords = list()
        self.color = random.randint(1, 6)
        for i in range(len(self.blocks[block_type])):
            for j in range(len(self.blocks[block_type][i])):
                if self.blocks[block_type][i][j] == 1:
                    self.coords.append([Constant.START_X + j * Constant.BLOCK,
                                        Constant.START_Y + i * Constant.BLOCK])
                    self.blocks[block_type][i][j] = 2
        for square in self.coords:
            Square(block_type, square[0], square[1], self.color, *groups)