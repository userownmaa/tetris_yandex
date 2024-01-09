from constant import Constant
from square import Square


class ActiveBlock:

    blocks = {
        "O": [[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]],
        "T": [[0, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 0, 0],
              [0, 0, 0, 0]],
        "I": [[0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0]],
        "L": [[0, 0, 1, 0],
              [1, 1, 1, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]],
        "Z": [[0, 0, 0, 0],
              [1, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]],
        "Z_rev": [[0, 0, 0, 0],
                  [0, 1, 1, 0],
                  [1, 1, 0, 0],
                  [0, 0, 0, 0]],
        "L_rev": [[1, 0, 0, 0],
                  [1, 1, 1, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
    }

    def __init__(self, block_type, *groups):
        self.matrix = self.blocks[block_type]
        self.coords = list()
        for i in range(len(self.blocks[block_type])):
            for j in range(i):
                if self.blocks[block_type][i][j] == 1:
                    self.coords.append([Constant.MARGIN_LEFT + (j+1) * Constant.BLOCK,
                                              Constant.MARGIN_TOP + (i+1) * Constant.BLOCK])
                    self.blocks[block_type][i][j] = 2
        for square in self.coords:
            Square("O", square[0], square[1], *groups)