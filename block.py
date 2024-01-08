class Block:
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

    def __init__(self, block_type):
        self.matrix = self.blocks[block_type]

    def turn(self):
        self.matrix =  # повернуть матрицу

    def down(self):
        self.matrix = # опустить блок