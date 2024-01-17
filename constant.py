import pygame


class Constant:
    # BLOCKS_MATRIX = {
    #     "O": [[0, 0, 0, 0],
    #           [0, 1, 1, 0],
    #           [0, 1, 1, 0],
    #           [0, 0, 0, 0]],
    #     "T": [[0, 0, 0, 0],
    #           [0, 1, 0, 0],
    #           [0, 1, 1, 0],
    #           [0, 1, 0, 0]],
    #     "I": [[0, 0, 0, 0],
    #           [1, 1, 1, 1],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]],
    #     "L": [[0, 0, 0, 0],
    #           [0, 1, 1, 0],
    #           [0, 1, 0, 0],
    #           [0, 1, 0, 0]],
    #     "Z": [[0, 0, 0, 0],
    #           [1, 1, 0, 0],
    #           [0, 1, 1, 0],
    #           [0, 0, 0, 0]],
    #     "Z_rev": [[0, 0, 0, 0],
    #               [0, 1, 1, 0],
    #               [1, 1, 0, 0],
    #               [0, 0, 0, 0]],
    #     "L_rev": [[0, 0, 0, 0],
    #               [1, 1, 0, 0],
    #               [0, 1, 0, 0],
    #               [0, 1, 0, 0]]
    # }

    BLOCKS_START_POSITION = {
        "O": [[1, 1], [2, 1], [1, 2], [2, 2]],
        "T": [[1, 1], [1, 2], [2, 2], [1, 3]],
        "I": [[0, 1], [1, 1], [2, 1], [3, 1]],
        "L": [[1, 1], [2, 1], [1, 2], [1, 3]],
        "Z": [[0, 1], [1, 1], [1, 2], [2, 2]],
        "Z_rev": [[1, 1], [2, 1], [0, 2], [1, 2]],
        "L_rev": [[0, 1], [1, 1], [1, 2], [1, 3]]
    }

    BLOCKS_POSITION_1 = {
        "O": [[0, 0], [0, 0], [0, 0], [0, 0]],
        "T": [[1, -1], [0, 0], [1, 1], [-1, 1]],
        "I": [[-1, -2], [0, -1], [1, 0], [2, 1]],
        "L": [[1, -1], [2, 0], [0, 0], [-1, 1]],
        "Z": [[0, -2], [1, -1], [0, 0], [1, 1]],
        "Z_rev": [[1, -1], [2, 0], [-1, -1], [0, 0]],
        "L_rev": [[0, 2], [1, -1], [0, 0], [-1, 1]]
    }
    BLOCKS_POSITION_2 = {
        "O": [[0, 0], [0, 0], [0, 0], [0, 0]],
        "T": [[1, 1], [0, 0], [-1, 1], [-1, -1]],
        "I": [[2, -1], [1, 0], [0, 1], [-1, 2]],
        "L": [[1, 1], [0, 2], [0, 0], [-1, -1]],
        "Z": [[2, 0], [1, 1], [0, 0], [-1, 1]],
        "Z_rev": [[1, 1], [0, 2], [1, -1], [0, 0]],
        "L_rev": [[2, 0], [1, 1], [0, 0], [-1, -1]]
    }
    BLOCKS_POSITION_3 = {
        "O": [[0, 0], [0, 0], [0, 0], [0, 0]],
        "T": [[-1, 1], [0, 0], [-1, -1], [1, -1]],
        "I": [[1, 2], [0, 1], [-1, 0], [-1, -2]],
        "L": [[-1, 1], [-2, 0], [0, 0], [1, -1]],
        "Z": [[0, 2], [-1, 1], [0, 0], [-1, -1]],
        "Z_rev": [[-1, 1], [-2, 0], [1, 1], [0, 0]],
        "L_rev": [[0, 2], [-1, 1], [0, 0], [1, -1]]
    }
    BLOCKS_POSITION_4 = {
        "O": [[0, 0], [0, 0], [0, 0], [0, 0]],
        "T": [[-1, -1], [0, 0], [1, -1], [1, 1]],
        "I": [[-2, 1], [-1, 0], [0, -1], [1, -2]],
        "L": [[-1, -1], [0, -2], [0, 0], [1, 1]],
        "Z": [[-2, 0], [-1, -1], [0, 0], [1, -1]],
        "Z_rev": [[-1, -1], [2, 0], [-1, -1], [0, 0]],
        "L_rev": [[-2, 0], [-1, -1], [0, 0], [1, 1]]
    }

    BLACK = pygame.Color("black")
    WHITE = pygame.Color("white")

    SIZE = WIDTH, HEIGHT = (600, 500)
    FPS = 50
    # SIDE_SPEED = 0.15
    BLOCK = 20
    FIELD_WIDTH, FIELD_HEIGHT = 10, 20
    # MARGIN_LEFT = (WIDTH - FIELD_WIDTH * BLOCK) // 2
    MARGIN_LEFT = 10
    # MARGIN_TOP = HEIGHT - (FIELD_HEIGHT * BLOCK) - 20
    MARGIN_TOP = 4
    BOTTOM_BORDER = 24
    # RIGHT_BORDER = WIDTH - MARGIN_LEFT
    RIGHT_BORDER = 20
    # LEFT_BORDER = WIDTH - MARGIN_LEFT - FIELD_WIDTH  # - BLOCK
    LEFT_BORDER = 9
    # START_X = MARGIN_LEFT + BLOCK * 3
    START_X = 13
    # START_Y = MARGIN_TOP
    START_Y = 3

    DOWN_X = 0
    DOWN_Y = 20
    UP_X = 0
    UP_Y = -20
    LEFT_X = -20
    LEFT_Y = 0
    RIGHT_X = 20
    RIGHT_Y = 0