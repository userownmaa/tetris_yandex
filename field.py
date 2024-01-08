from constant import Constant


class Field:

    def __init__(self):
        self.matrix = [[0] * Constant.WIDTH for i in range(Constant.HEIGHT)]
