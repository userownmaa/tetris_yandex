import sys
import pygame

from active_block import ActiveBlock
from constant import Constant
from field import Field
from image import Image


class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.active_block_group = pygame.sprite.Group()
        self.next_block_group = pygame.sprite.Group()
        self.bottom_group = pygame.sprite.Group()

    def start_screen(self, screen, clock):
        intro_text = []

        fon = pygame.transform.scale(Image.load_image(""), (Constant.WIDTH, Constant.HEIGHT))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, Constant.BLACK)
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return
            pygame.display.flip()
            clock.tick(Constant.FPS)

    def run_game(self, screen):
        field = Field()
        field.draw_field(screen)
        # рандомно выбрать форму
        block = ActiveBlock("I", self.all_sprites, self.active_block_group)
        self.all_sprites.draw(screen)



    def terminate(self):
        pygame.quit()
        sys.exit()
