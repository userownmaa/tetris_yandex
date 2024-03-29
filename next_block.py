from constant import Constant
from square import Square


class NextBLock:
    def __init__(self, block_type, color, *groups):
        self.block_type = block_type
        self.color = color
        for square in Constant.NEXT_BLOCKS_START_POSITION[block_type]:
            Square(square[0], square[1], self.color, *groups)

    def close(self, next_block_group):
        for sprite in next_block_group:
            sprite.kill()

    def get_type(self):
        return self.block_type

