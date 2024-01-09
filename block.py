from image import Image
import random

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

    color_blocks = {
        1: Image.load_image(""),
        2: Image.load_image(""),
        3: Image.load_image(""),
        4: Image.load_image(""),
        5: Image.load_image(""),
        6: Image.load_image("")
    }

    def __init__(self, block_type):
        self.matrix = self.blocks[block_type]
        self.image = self.color_blocks[random.randint(1, 6)]

    def turn(self):
        self.matrix =  # повернуть матрицу

    def get_image(self):
        return self.image