import pygame

from constant import Constant


class Field:

    def __init__(self):
        self.n = 0
        self.completed = list()
        self.matrix = [[0] * Constant.FIELD_WIDTH for i in range(Constant.FIELD_HEIGHT)]

    def draw_field(self, screen):
        for y in range(Constant.FIELD_HEIGHT):
            for x in range(Constant.FIELD_WIDTH):
                pygame.draw.rect(screen, Constant.WHITE, (Constant.MARGIN_LEFT * Constant.BLOCK + x * Constant.BLOCK,
                                                          Constant.MARGIN_TOP * Constant.BLOCK + y * Constant.BLOCK,
                                                          Constant.BLOCK, Constant.BLOCK), 1)
        pygame.draw.rect(screen, Constant.WHITE, (Constant.SMALL_FIELD_X * Constant.BLOCK,
                                                  Constant.SMALL_FIELD_Y * Constant.BLOCK,
                                                  Constant.SMALL_FIELD_WIDTH, Constant.SMALL_FIELD_HEIGHT), 1)

    def draw_frame(self, screen, block_type):
        for pos in Constant.NEXT_BLOCKS_START_POSITION[block_type]:
            pygame.draw.rect(screen, Constant.WHITE, (pos[0] - 1, pos[1] - 1,
                                                      Constant.BLOCK + 1, Constant.BLOCK + 1), 1)

    def is_row_completed(self, bottom_group):
        ordinates = list()
        for sprite in bottom_group:
            ordinates.append(sprite.get_position()[1])
        for y in ordinates:
            if ordinates.count(y) >= 10:
                self.completed.append(y)
        self.n = len(self.completed)
        if self.completed:
            return True
        return False

    def clear_row(self, bottom_group):
        for y in self.completed:
            for sprite in bottom_group:
                if sprite.get_position()[1] == y:
                    sprite.kill()

    def drop_rows(self, bottom_group):
        for sprite in bottom_group:
            x, y = sprite.get_position()[0], sprite.get_position()[1]
            if y <= max(self.completed):
                sprite.move_down(x * Constant.BLOCK, y * Constant.BLOCK * self.n)





