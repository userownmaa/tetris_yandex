import pygame
import sys
from constant import Constant
from game import Game

pygame.init()
screen = pygame.display.set_mode(Constant.SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("TETRIS")
game = Game()


def main():
    game.start_screen(screen, clock)
    running = True
    while running:
        clock.tick(Constant.FPS)
        screen.fill(Constant.BLACK)
        running = game.run_game(screen)
        pygame.display.flip()
    game.finish_screen(screen, clock)
    game.terminate()


if __name__ == '__main__':
    sys.exit(main())